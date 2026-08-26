# The Exclusion Ratchet

Measuring how false-positive suppression accumulates and persists in detection-rule
repositories, across nine years of the public SigmaHQ corpus.

Analysis code and derived data for the paper *The Exclusion Ratchet: False-Positive
Suppression Accumulates and Persists in Detection Rule Repositories* (under review).

## The question

When a detection rule produces too many false alarms, a maintainer adds an exclusion.
Each decision is locally reasonable. What becomes of them collectively is not known.

Prior longitudinal work measured how long a revision lasts before being reverted — but
only for revisions that *were* reverted. Narrowing that is never undone is invisible to
a measure conditioned on reversion, and that is the population this study measures.

## What it found

| | |
|---|---|
| Suppressions / relaxations | 1,642 : 304 — **5.4 : 1** |
| Per rule, among rules that ever modified their exclusions | 481 : 37 — **13 : 1** |
| Narrowing invisible to structural comparison | **31%** (503 of 1,642) |
| Exclusions still in force after three years | **86.7%** (Kaplan–Meier, n = 1,584) |
| Persistence by coverage redundancy | **no difference** (log-rank p = 0.49) |
| Path exclusions enterable without privilege | **64.1%**; 33.0% require privileged write |
| Broad *and* freely enterable — examine these first | **12.3%** |
| Detector precision / recall | 0.828 [0.711, 0.904] / 0.911 |

Corpus: 2,355 rule lineages, 8,234 predicate-changing revisions, 27 December 2016 to a
snapshot of 10 April 2026.

## Layout

    src/detector.py       canonical definitions of suppression and relaxation
    src/forgeability.py   attribute classification and path-anchor taxonomy
    src/tagmap.py         lineage -> MITRE ATT&CK technique mapping
    src/figures.py        Figures 1, 5, 6 and the anchor breakdown
    src/fig3_persistence.py   the survival curve and the coverage null
    src/fig_timeline.py   the single-rule exclusion history (Figure 7)
    src/score_validation.py   precision and stratified recall from the labels

    notebooks/analysis.ipynb  the derivation record: every CSV in results/ comes from here
    results/              derived data, figures, and the full session record
    results/validation/   the 120-item sample, its labels, and the worksheet
    docs/                 lab notebook, explainers, and the superseded structural classifier

**Definitions live in `src/detector.py` and are imported, never restated.** Divergence
between a cell-local copy of a definition and the module caused two of the nine
corrections recorded in `results/2026-08-20.md`; do not paste a definition into a cell.

## Reproducing

Two external inputs are required and neither is committed. See `data/README.md`.

    git clone https://github.com/SigmaHQ/sigma.git ../sigma      # full history, no --depth
    # prepared pipeline outputs from Long & Evans into
    # ../Evolution-of-Log-Based-Detection-Rules/data_prep/   (~1.9 GB)

Then:

    python -m venv venv && source venv/Scripts/activate
    pip install -r requirements.txt

    python src/tagmap.py              # lineage -> ATT&CK mapping
    jupyter lab notebooks/analysis.ipynb   # run all; writes results/*.csv
    python src/figures.py
    python src/fig3_persistence.py
    python src/fig_timeline.py
    python src/score_validation.py

The notebook reaches into the upstream checkout for the prepared data and the alignment
helpers, and writes nothing to it.

Environment: Python 3.14.6, pandas 2.3.3, numpy 2.4.0, lifelines 0.30.3,
matplotlib 3.10.8. Pinned in `requirements.txt`.

## Validation

The detector was checked against hand labelling rather than asserted. 120 revision
steps were drawn, shuffled, and presented as predicate differences with commit messages
withheld, so that the commit-message corroboration reported in the paper remains
independent of the labels. The sample, the labels and the worksheet are in
`results/validation/`. Items discussed with an AI assistant during labelling are flagged
in the label file so that any reader may exclude them and recompute.

Nine corrections were made to the method during the work. All are recorded, with their
effect on the reported numbers, in `results/2026-08-20.md`. Three narrowing mechanisms
remain undetected and all three bias the reported ratio downward, so 5.4 : 1 is a floor.

## Prior work

Minjun Long and David Evans, *Evolution of Log-Based Detection Rules in Public
Repositories*, arXiv:2605.05383. Their pipeline and prepared corpus made this study
possible, and their Tables 5 and 6 were reproduced exactly before anything was extended.

Four discrepancies between that paper and its released artefact were found during
reproduction and reported to the authors; they are set out in Appendix A of the paper.
One of them matters to anyone else building on the bundle: **joining commit metadata by
treating `version_index` as a position in a lineage's `commits` list recovers the correct
commit only 19.7% of the time**, because a filter applied before analysis drops versions
whose SPL will not parse and the two lists diverge thereafter. The failure is silent and
produces a plausible result. Join on commit date or hash.

## Use of AI tools

Analysis and figure code was written and reviewed with AI assistance; 15 of the 120
validation items were discussed with an assistant during labelling and are flagged in
the released labels. No measurement reported in the paper was produced, selected or
interpreted by a model. Tool, model version and dates are recorded in `AI_USE.md`.

## Licence

Analysis code MIT. Upstream data remains under its original licences.
