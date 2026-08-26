r"""
Figure 7 — the exclusion history of a single rule.

The worked example for Section 5.7. One bar per distinct exclusion, running from the
revision that introduced it to the revision that last carried it, or to the snapshot if
it is still in force. It is the persistence finding made concrete on one rule.

Default lineage is lineage_02731, rules/windows/image_load/image_load_dll_vss_ps_susp_load.yml,
chosen because its history shows four things the paper argues separately:

  * steady accretion over four years, in ten distinct episodes
  * 24 of 27 exclusions still in force at the snapshot
  * the three that lapse are not reconsiderations but re-spellings — '*dismhost.exe'
    and '*taskhostw.exe' return eleven months later as '*\dismhost.exe' and
    '*\taskhostw.exe', which is the case-variant limitation of Section 4.3 visible in
    a single rule
  * escalation from named binaries to whole directory trees on 2022-10-31

Reads the upstream cache and version metadata directly; writes results/fig_timeline.{png,pdf}.

Run:  python src/fig_timeline.py [lineage_id]
"""

import json
import pathlib
import pickle
import sys
from collections import defaultdict

import matplotlib
matplotlib.use("Agg")
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
from detector import literals, neg_preds_fields, norm          # noqa: E402

UPSTREAM = ROOT.parent / "Evolution-of-Log-Based-Detection-Rules"
CACHE = UPSTREAM / "analysis/scripts/.cache/struct_ops_sigma.pkl"
VERSIONS = UPSTREAM / "data_prep/build_data/rule_versions_sigma.jsonl"
METADATA = UPSTREAM / "data_prep/build_data/lineage_metadata_final_sigma.json"
RESULTS = ROOT / "results"

SNAPSHOT = pd.Timestamp("2026-04-10", tz="UTC")
LINEAGE = sys.argv[1] if len(sys.argv) > 1 else "lineage_02731"
MIN_BAR = 45          # days; so a short-lived exclusion is still visible

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "DejaVu Sans"],
    "font.size": 9,
    "axes.linewidth": 0.8,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
})

# a literal naming a directory tree rather than one file
BROAD = ("\\*", "/*")


def load():
    with CACHE.open("rb") as fh:
        res = pickle.load(fh)["results"]

    date_of = {}
    with VERSIONS.open(encoding="utf-8") as fh:
        for line in fh:
            r = json.loads(line)
            date_of[(r["lineage_id"], r["version_index"])] = \
                pd.to_datetime(r["commit_date"], utc=True)

    names = {e["lineage_id"]: (e.get("canonical_name")
                               or (e.get("all_paths") or [""])[0])
             for e in json.loads(METADATA.read_text(encoding="utf-8"))}
    return res, date_of, names


def exclusion_spans(res, date_of, lineage):
    """(first seen, last seen, still present, field, value) per distinct exclusion."""
    def pairs(sig):
        return {(f, norm(v)) for f, p in neg_preds_fields(sig) for v in literals(p)}

    versions = {}
    for step in (s for s in res if s["lineage_id"] == lineage):
        for vi, sig in ((step["version_a"], step["sig_a"]),
                        (step["version_b"], step["sig_b"])):
            versions.setdefault(vi, (date_of.get((lineage, vi)), pairs(sig)))

    order = [v for v in sorted(versions) if versions[v][0] is not None]
    seen = defaultdict(list)
    for v in order:
        for pair in versions[v][1]:
            seen[pair].append(v)

    rows = []
    for (field, value), vs in seen.items():
        rows.append((versions[min(vs)][0], versions[max(vs)][0],
                     max(vs) == order[-1], field, value))
    rows.sort(key=lambda r: (r[0], r[3], r[4]))
    return rows, versions[order[0]][0], versions[order[-1]][0]


def main():
    res, date_of, names = load()
    rows, first, last = exclusion_spans(res, date_of, LINEAGE)
    live = sum(1 for r in rows if r[2])
    rule = pathlib.PurePosixPath(str(names.get(LINEAGE, LINEAGE))).name

    fig, ax = plt.subplots(figsize=(6.4, 0.205 * len(rows) + 1.15))

    for i, (t0, t1, alive, field, value) in enumerate(rows):
        end = SNAPSHOT if alive else t1
        width = max((end - t0).days, MIN_BAR)
        ax.barh(i, width, left=t0, height=0.62,
                color="0.28" if alive else "white",
                edgecolor="0.28" if alive else "0.55",
                linewidth=0 if alive else 0.7,
                hatch=None if alive else "///", zorder=3)

    labels = [f"{f}: {v}" + ("  †" if v.endswith(BROAD) else "")
              for _, _, _, f, v in rows]
    ax.set_yticks(range(len(rows)))
    ax.set_yticklabels(labels, fontsize=6.2, fontfamily="monospace")
    ax.invert_yaxis()

    ax.axvline(SNAPSHOT, color="0.35", linewidth=0.8, linestyle=":", zorder=2)
    # bottom of the axis, so it cannot collide with the two-line title
    ax.annotate("snapshot", xy=(SNAPSHOT, len(rows) - 0.4),
                xytext=(-3, 0), textcoords="offset points",
                fontsize=6.5, color="0.35", ha="right", va="bottom", rotation=90)

    ax.set_xlim(first - pd.Timedelta(days=90), SNAPSHOT + pd.Timedelta(days=150))
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax.tick_params(axis="x", labelsize=7.5)
    ax.tick_params(axis="y", length=0)
    ax.grid(axis="x", color="0.88", linewidth=0.6, zorder=0)
    ax.set_axisbelow(True)

    ax.set_title(f"{rule}\n{len(rows)} exclusions added over "
                 f"{(last - first).days // 365} years · {live} still in force at the "
                 f"snapshot ({100 * live / len(rows):.0f}%)",
                 fontsize=8.5, loc="left", pad=8)

    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)

    handles = [plt.Rectangle((0, 0), 1, 1, facecolor="0.28", edgecolor="none"),
               plt.Rectangle((0, 0), 1, 1, facecolor="white", edgecolor="0.55",
                             hatch="///", linewidth=0.7)]
    ax.legend(handles, ["in force at the snapshot", "no longer present"],
              frameon=False, fontsize=6.8, ncol=2, loc="lower right",
              bbox_to_anchor=(1.0, -0.055 - 0.9 / len(rows)))

    fig.tight_layout()
    RESULTS.mkdir(exist_ok=True)
    for ext in ("png", "pdf"):
        fig.savefig(RESULTS / f"fig_timeline.{ext}",
                    dpi=600 if ext == "png" else None, bbox_inches="tight")
    plt.close(fig)

    print(f"{LINEAGE}  {rule}")
    print(f"  {len(rows)} exclusions, {live} in force at snapshot "
          f"({100 * live / len(rows):.0f}%)")
    print(f"  {first.date()} → {last.date()}  ({(last - first).days} days)")
    print(f"  wrote {RESULTS / 'fig_timeline.png'} and .pdf")


if __name__ == "__main__":
    main()
