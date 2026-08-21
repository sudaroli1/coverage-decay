"""
Score the blinded validation sample for the suppression detector.

Inputs (both in results/validation/):
    sample_key.csv     item_id, lineage, version_a, version_b, arm, stratum, stratum_size
                       arm = 'pos' (detector said suppression) | 'neg' (it did not)
    sample_labels.csv  item_id, label            label in {S, N, U}
                       S = a human reading the diff calls it a suppression

Outputs precision, an estimated recall, and Wilson 95% intervals.

Recall is estimated, not observed: false negatives are counted in each negative
stratum and scaled up by that stratum's size in the corpus, since negatives were
sampled disproportionately. Unlabelled and 'U' items are dropped and reported.

Run:  python src/score_validation.py
"""

import csv
import pathlib
from collections import defaultdict

ROOT = pathlib.Path(__file__).resolve().parent.parent
VAL = ROOT / "results" / "validation"


def wilson(k, n, z=1.96):
    """Wilson score interval — behaves sanely at k=0 and k=n, unlike the normal approx."""
    if n == 0:
        return (0.0, 1.0)
    p = k / n
    d = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / d
    half = z * ((p * (1 - p) / n + z * z / (4 * n * n)) ** 0.5) / d
    return (max(0.0, centre - half), min(1.0, centre + half))


def load():
    key = {r["item_id"]: r for r in csv.DictReader(open(VAL / "sample_key.csv", encoding="utf-8"))}
    lab = {r["item_id"]: r["label"].strip().upper()
           for r in csv.DictReader(open(VAL / "sample_labels.csv", encoding="utf-8"))
           if r["label"].strip()}
    return key, lab


def main():
    key, lab = load()
    n_total = len(key)
    unlabelled = n_total - len(lab)
    unclear = sum(1 for v in lab.values() if v == "U")

    pos = [(i, lab[i]) for i in key if key[i]["arm"] == "pos" and lab.get(i) in ("S", "N")]
    tp = sum(1 for _, l in pos if l == "S")
    fp = len(pos) - tp
    prec = tp / len(pos) if pos else 0.0
    plo, phi = wilson(tp, len(pos))

    print(f"labelled {len(lab)}/{n_total}   unclear {unclear}   unlabelled {unlabelled}\n")
    print("PRECISION")
    print(f"  sampled positives : {len(pos)}")
    print(f"  true suppressions : {tp}")
    print(f"  false positives   : {fp}")
    print(f"  precision         : {prec:.3f}   95% CI [{plo:.3f}, {phi:.3f}]\n")

    # false negatives, per stratum, scaled to corpus
    by_str = defaultdict(lambda: {"n": 0, "fn": 0, "size": 0})
    for i, r in key.items():
        if r["arm"] != "neg" or lab.get(i) not in ("S", "N"):
            continue
        b = by_str[r["stratum"]]
        b["n"] += 1
        b["size"] = int(r["stratum_size"])
        b["fn"] += (lab[i] == "S")

    print("FALSE NEGATIVES BY STRATUM")
    est_fn = 0.0
    for name, b in sorted(by_str.items()):
        rate = b["fn"] / b["n"] if b["n"] else 0.0
        lo, hi = wilson(b["fn"], b["n"])
        scaled = rate * b["size"]
        est_fn += scaled
        print(f"  {name:<34} {b['fn']:>3}/{b['n']:<3} = {rate:5.3f} "
              f"[{lo:.3f},{hi:.3f}]  x{b['size']:<5} -> {scaled:7.1f}")

    detected = int(key[next(iter(key))].get("n_detected", 0)) or None
    if detected is None:
        print("\n(n_detected missing from key; pass the sup2 size to finish recall)")
        return

    est_tp = prec * detected
    recall = est_tp / (est_tp + est_fn) if (est_tp + est_fn) else 0.0
    print(f"\nRECALL (estimated)")
    print(f"  detected suppressions      : {detected}")
    print(f"  estimated true positives   : {est_tp:.0f}")
    print(f"  estimated false negatives  : {est_fn:.0f}")
    print(f"  recall                     : {recall:.3f}")
    print(f"  implied true population    : {est_tp + est_fn:.0f}")
    print("\nRecall is a point estimate from stratified sampling; report the per-stratum")
    print("intervals above alongside it rather than a single CI.")


if __name__ == "__main__":
    main()
