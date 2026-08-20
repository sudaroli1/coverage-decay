# Detection rule coverage decay

Measuring what false-positive suppression costs in detection coverage, across nine
years of the public Sigma detection-rule corpus.

## Question

Security teams suppress false alarms by adding exclusions to detection rules. Each
exclusion narrows what the rule catches for as long as it persists. Prior longitudinal
analysis of this corpus measured how long changes last before being reverted — but only
for changes that *were* reverted. Suppressions never removed are excluded from that
measurement, and those are the durable blind spots.

This study measures them.

## Method

1. Reproduce Long & Evans (arXiv:2605.05383) to establish the baseline.
2. Detect suppression semantically: a step where the count of predicates in negated
   context grows is an exclusion growing, which is a narrowing of detection.
3. Join rule lineages to MITRE ATT&CK techniques via Sigma rule UUIDs.
4. Identify techniques covered by exactly one rule, where a suppression removes
   coverage outright rather than reducing redundancy.
5. Measure how long each suppression persists, treating suppressions still in place
   at the snapshot date as right-censored.

## Status

Reproduction complete. Suppression detection implemented. Hand-validation pending.

## Reproducing

    python -m venv venv && source venv/Scripts/activate
    pip install -r requirements.txt
    # obtain data — see data/README.md
    python src/tagmap.py      # build lineage -> ATT&CK mapping
    python src/suppress.py    # suppression detection and exposure measurement

## Prior work

Minjun Long and David Evans, "Evolution of Log-Based Detection Rules in Public
Repositories", arXiv:2605.05383. Their pipeline and prepared data made this study
possible. Reproduction notes, including four discrepancies found and reported to the
authors, are in `docs/`.

## Licence

Analysis code MIT. Upstream data remains under its original licences.
