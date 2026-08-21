"""
Figure 3 — persistence of detection-rule exclusions.

Reads results/survival_suppressions.csv, which is exported from the analysis
notebook by:

    surv.to_csv('.../results/survival_suppressions.csv', index=False)

Columns expected: lineage, suppressed_on, days, removed, min_coverage, group

Produces:
    results/fig3_persistence.png   main curve, all suppressions, horizon markers
    results/fig4_null_coverage.png sole vs redundant coverage (the null result)

Run:  python src/fig3_persistence.py
"""

import pathlib
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from lifelines import KaplanMeierFitter
from lifelines.statistics import logrank_test
from lifelines.utils import restricted_mean_survival_time as rmst

ROOT = pathlib.Path(__file__).resolve().parent.parent
RESULTS = ROOT / "results"

# Elsevier figures: no colour dependence, embeddable fonts, 600 dpi line art.
plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "DejaVu Sans"],
    "font.size": 9,
    "axes.linewidth": 0.8,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
})

HORIZONS = [180, 365, 730, 1095]


def load():
    surv = pd.read_csv(RESULTS / "survival_suppressions.csv")
    surv = surv[surv["days"] >= 1]
    return surv


def figure3(surv):
    kmf = KaplanMeierFitter().fit(surv["days"], surv["removed"])

    fig, ax = plt.subplots(figsize=(5.5, 3.6))
    kmf.plot_survival_function(
        ax=ax, ci_show=True, color="0.15", linewidth=1.3,
        show_censors=True, censor_styles={"ms": 2.0, "marker": "|", "alpha": 0.18},
        legend=False,
    )

    # leave headroom below the lowest confidence bound, but never crop the band
    lo = float(kmf.confidence_interval_.iloc[:, 0].min())
    ymin = max(0.0, min(0.70, lo - 0.03))

    for d in HORIZONS:
        s = float(kmf.predict(d))
        ax.plot([d, d], [ymin, s], color="0.55", linewidth=0.6, linestyle=":")
        ax.plot([0, d], [s, s], color="0.55", linewidth=0.6, linestyle=":")
        ax.annotate(f"{s:.3f}", xy=(d, s), xytext=(6, 4),
                    textcoords="offset points", fontsize=7.5, color="0.25")

    ax.set_xlim(0, surv["days"].max() * 1.02)
    ax.set_ylim(ymin, 1.0)
    ax.set_xlabel("Days since exclusion added")
    ax.set_ylabel("Fraction of exclusions still in place")
    ax.set_xticks([0, 180, 365, 730, 1095, 1825, 2555, 3285])
    ax.tick_params(labelsize=8)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)

    n, ev = len(surv), int(surv["removed"].sum())
    ax.text(0.98, 0.96,
            f"n = {n:,} exclusions\n{ev} removed, {n - ev:,} censored ({100*(1-ev/n):.1f}%)",
            transform=ax.transAxes, ha="right", va="top", fontsize=7.5, color="0.25")

    fig.tight_layout()
    out = RESULTS / "fig3_persistence.png"
    fig.savefig(out, dpi=600)
    fig.savefig(out.with_suffix(".pdf"))
    plt.close(fig)

    return kmf, out


def figure4(surv):
    a = surv[surv["group"] == "singleton"]
    b = surv[surv["group"] == "redundant"]
    if a.empty or b.empty:
        return None, None

    fig, ax = plt.subplots(figsize=(5.5, 3.6))
    for df, label, style in (
        (a, f"sole coverage (n = {len(a)})", {"color": "0.15", "linestyle": "-"}),
        (b, f"redundant coverage (n = {len(b)})", {"color": "0.45", "linestyle": "--"}),
    ):
        KaplanMeierFitter().fit(df["days"], df["removed"], label=label) \
            .plot_survival_function(ax=ax, ci_show=True, linewidth=1.2, **style)

    r = logrank_test(a["days"], b["days"], a["removed"], b["removed"])
    ax.text(0.98, 0.06, f"log-rank $p$ = {r.p_value:.2f}",
            transform=ax.transAxes, ha="right", va="bottom", fontsize=8, color="0.25")

    ax.set_ylim(0.60, 1.0)
    ax.set_xlabel("Days since exclusion added")
    ax.set_ylabel("Fraction of exclusions still in place")
    ax.legend(frameon=False, fontsize=8, loc="upper right")
    ax.tick_params(labelsize=8)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)

    fig.tight_layout()
    out = RESULTS / "fig4_null_coverage.png"
    fig.savefig(out, dpi=600)
    fig.savefig(out.with_suffix(".pdf"))
    plt.close(fig)

    return r, out


def main():
    surv = load()
    kmf, f3 = figure3(surv)
    r, f4 = figure4(surv)

    print(f"n = {len(surv)}   removed = {int(surv['removed'].sum())}   "
          f"censored = {int((surv['removed'] == 0).sum())} "
          f"({100*(surv['removed'] == 0).mean():.1f}%)")
    print("\nsurvival at fixed horizons")
    for d in [30, 90, 180, 365, 730, 1095]:
        print(f"  S({d:>4}d) = {float(kmf.predict(d)):.3f}")

    print(f"\nKM median survival : {kmf.median_survival_time_}")
    print(f"RMST over 3 years  : {rmst(kmf, t=1095):.0f} days")

    kmf_c = KaplanMeierFitter().fit(surv["days"], 1 - surv["removed"])
    print(f"median follow-up   : {kmf_c.median_survival_time_:.0f} days")

    rem = surv[surv["removed"] == 1]
    print(f"\nremovals within 180d : {100*(rem['days'] <= 180).mean():.0f}%")
    print(f"removals within 365d : {100*(rem['days'] <= 365).mean():.0f}%")

    if r is not None:
        print(f"\nlog-rank p = {r.p_value:.4g}   statistic = {r.test_statistic:.2f}")

    print(f"\nwrote {f3.name}" + (f", {f4.name}" if f4 else ""))


if __name__ == "__main__":
    main()
