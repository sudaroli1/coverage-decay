"""
Figures 1, 2, 4 and 5 for the exclusion-ratchet paper.

Reads the CSVs exported from the analysis notebook:
    results/events.csv            lineage, date, kind, mechanism, age_days
    results/activity_monthly.csv  month, all_revisions
    results/lineage_births.csv    birth
    results/anchor_counts.csv     anchor, n

Writes to results/, each as .png (600 dpi) and .pdf:
    fig_cumulative   net exclusion burden over time, raw and per active rule
    fig_ruleage      rule age when an exclusion is added
    fig_sharetrend   suppression share of all revisions, by mechanism
    fig_anchor       whether path exclusions can be entered, and at what cost

Figure 3 (persistence) and the coverage null are produced by fig3_persistence.py.

Run:  python src/figures.py
"""

import pathlib
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

ROOT = pathlib.Path(__file__).resolve().parent.parent
R = ROOT / "results"

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "DejaVu Sans"],
    "font.size": 9,
    "axes.linewidth": 0.8,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
})

MIN_DENOM = 50   # months with fewer revisions give meaningless shares


def save(fig, name):
    fig.tight_layout()
    fig.savefig(R / f"{name}.png", dpi=600)
    fig.savefig(R / f"{name}.pdf")
    plt.close(fig)
    print(f"  wrote {name}")


def tidy(ax):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.tick_params(labelsize=8)


def load():
    ev = pd.read_csv(R / "events.csv", parse_dates=["date"])
    act = pd.read_csv(R / "activity_monthly.csv", index_col=0, parse_dates=True)
    births = pd.read_csv(R / "lineage_births.csv", parse_dates=["birth"])
    anchor = pd.read_csv(R / "anchor_counts.csv", index_col=0)
    return ev, act.iloc[:, 0], births["birth"], anchor.iloc[:, 0]


def fig_cumulative(ev, births):
    """Net exclusions added over time — raw, and normalised by active rules.

    The lower panel is the one that matters: it answers the objection that
    accumulation merely reflects a growing corpus.
    """
    s = ev.assign(x=ev.kind.map({"suppression": 1, "relaxation": -1})) \
          .set_index("date").sort_index()
    net = s.x.resample("ME").sum().cumsum()
    alive = pd.Series(1, index=pd.DatetimeIndex(births)).sort_index() \
              .resample("ME").sum().cumsum().reindex(net.index, method="ffill")

    fig, ax = plt.subplots(2, 1, figsize=(5.5, 4.8), sharex=True)
    ax[0].plot(net.index, net.values, color="0.15", linewidth=1.3)
    ax[0].set_ylabel("net exclusions added")
    ax[0].annotate(f"{net.iloc[-1]:,.0f}", xy=(net.index[-1], net.iloc[-1]),
                   xytext=(-4, -10), textcoords="offset points",
                   ha="right", fontsize=8, color="0.35")

    per = net / alive
    ax[1].plot(per.index, per.values, color="0.15", linewidth=1.3)
    ax[1].set_ylabel("per active rule")
    ax[1].set_xlabel("date")
    ax[1].annotate(f"{per.iloc[0]:.2f} → {per.iloc[-1]:.2f}",
                   xy=(0.02, 0.88), xycoords="axes fraction",
                   fontsize=8, color="0.35")
    for a in ax:
        tidy(a)
    save(fig, "fig_cumulative")


def fig_ruleage(ev):
    """How old a rule is when an exclusion is added."""
    age = ev.loc[(ev.kind == "suppression") & (ev.age_days >= 0), "age_days"]
    med = age.median()

    fig, ax = plt.subplots(figsize=(5.5, 3.2))
    ax.hist(age, bins=60, color="0.35", edgecolor="none")
    ax.axvline(med, color="0.1", linewidth=1, linestyle="--")
    ax.annotate(f"median {med:.0f} d", xy=(med, ax.get_ylim()[1] * 0.9),
                xytext=(6, 0), textcoords="offset points", fontsize=8, color="0.15")
    ax.set_xlabel("rule age when exclusion added (days)")
    ax.set_ylabel("suppressions")
    ax.annotate(f"{100*(age <= 90).mean():.0f}% within 90 days\n"
                f"{100*(age <= 365).mean():.0f}% within 1 year",
                xy=(0.97, 0.9), xycoords="axes fraction", ha="right",
                va="top", fontsize=8, color="0.35")
    tidy(ax)
    save(fig, "fig_ruleage")


def fig_sharetrend(ev, act):
    """Suppression as a share of all revision activity, split by mechanism.

    Split matters: value-level suppression needs an existing list to append to, so
    its opportunities grow structurally. A rise carried by the predicate mechanism
    cannot be explained that way.
    """
    sup = ev[ev.kind == "suppression"]
    idx = act.index

    def monthly(df):
        if df.empty:
            return pd.Series(0.0, index=idx)
        return pd.Series(1, index=pd.DatetimeIndex(df.date)).sort_index() \
                 .resample("ME").sum().reindex(idx).fillna(0)

    # Monthly shares are far too volatile to read a trend from directly, so the raw
    # series is shown faintly behind a 12-month rolling mean.
    ok = act >= MIN_DENOM
    fig, ax = plt.subplots(figsize=(5.5, 3.4))

    raw_all = (monthly(sup) / act)[ok]
    ax.plot(raw_all.index, raw_all.values, color="0.8", linewidth=0.7, zorder=1)

    for label, sub, style in (
        ("all suppressions", sup, {"color": "0.15", "linewidth": 1.5}),
        ("predicate-level", sup[sup.mechanism == "predicate"],
         {"color": "0.45", "linewidth": 1.1, "linestyle": "--"}),
        ("value-level", sup[sup.mechanism == "value"],
         {"color": "0.62", "linewidth": 1.1, "linestyle": ":"}),
    ):
        share = (monthly(sub) / act)[ok]
        roll = share.rolling(12, min_periods=6).mean()
        ax.plot(roll.index, roll.values, label=label, zorder=2, **style)

    ax.set_ylabel("share of monthly revisions")
    ax.set_xlabel("date")
    ax.set_ylim(bottom=0)
    ax.legend(frameon=False, fontsize=8, loc="upper left")
    ax.annotate(f"12-month rolling mean; raw monthly in grey\n"
                f"months with ≥{MIN_DENOM} revisions only",
                xy=(0.985, 0.97), xycoords="axes fraction", ha="right", va="top",
                fontsize=7.5, color="0.5")
    tidy(ax)
    save(fig, "fig_sharetrend")


def fig_anchor(anchor):
    """Can a path exclusion be entered, and at what cost."""
    free = ["bare name or suffix", "user-writable path"]
    cost = ["protected path"]
    other = [k for k in anchor.index if k not in free + cost]
    order = free + cost + other
    vals = [anchor.get(k, 0) for k in order]
    total = sum(vals)
    shades = ["0.25", "0.42", "0.72"] + ["0.88"] * len(other)

    fig, ax = plt.subplots(figsize=(5.5, 2.0))
    left = 0
    for k, v, c in zip(order, vals, shades):
        ax.barh(0, v, left=left, color=c, edgecolor="white", linewidth=0.8)
        if v / total > 0.05:
            ax.text(left + v / 2, 0, f"{100*v/total:.1f}%", ha="center",
                    va="center", fontsize=8.5,
                    color="white" if float(c) < 0.5 else "0.15")
        left += v

    ax.set_xlim(0, total)
    ax.set_ylim(-0.6, 0.6)
    ax.set_yticks([])
    ax.set_xlabel(f"path-valued exclusion literals (n = {total:,})")
    freen = sum(anchor.get(k, 0) for k in free)
    ax.set_title(f"{100*freen/total:.1f}% enterable without privilege   ·   "
                 f"{100*anchor.get('protected path',0)/total:.1f}% require privileged write",
                 fontsize=9.5, loc="left", pad=22)
    handles = [plt.Rectangle((0, 0), 1, 1, color=c) for c in shades[:3]]
    # legend sits between title and bar, so it cannot collide with the tick labels
    ax.legend(handles, ["bare name or suffix", "user-writable path", "protected path"],
              frameon=False, fontsize=7.5, ncol=3, loc="lower left",
              bbox_to_anchor=(0, 1.0), handlelength=1.4, columnspacing=1.4)
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    ax.tick_params(labelsize=8)
    save(fig, "fig_anchor")


def main():
    ev, act, births, anchor = load()
    print(f"{len(ev)} events, {len(act)} months, {len(births)} lineages")
    fig_cumulative(ev, births)
    fig_ruleage(ev)
    fig_sharetrend(ev, act)
    fig_anchor(anchor)


if __name__ == "__main__":
    main()
