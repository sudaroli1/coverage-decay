# Next session — 2026-08-21

Everything through detector validation is done and committed. Numbers are frozen;
they will not move again. Start here rather than re-reading `results/2026-08-20.md`.

## Setup (2 min)

```python
import sys; sys.path.insert(0, r'C:\Users\sudar\Desktop\Preparation\research\coverage-decay\src')
from detector import *
sup2 = [s for s in res if is_suppression(s)]      # 1,642
rel2 = [s for s in res if is_relaxation(s)]       # 304
```

Load `res`, `by_lin`, `date_of`, `SNAPSHOT`, `techs`, `cover` from your usual cells first.

## Morning plan

**0:00–0:30 — Figures 1 and 2 (mechanical).** Cumulative exclusion burden (§5.6.1) and
rule-age histogram (§5.6.4). Both are cells run yesterday; they need saving to
`results/` at 600 dpi with axis labels, following the style in `src/fig3_persistence.py`.
The per-active-rule panel matters more than the raw one — it's the panel that answers
the corpus-growth objection.

**0:30–1:00 — Figures 3 and 4 (mechanical).** Suppression-share trend (§5.6.5, plot only
months with ≥50 revisions) and the anchor breakdown as a horizontal stacked bar (§5.2:
58.2 / 33.0 / 5.9 / 2.4).

**1:00 onward — the worked-example timeline.** The one needing real thought, so give it
the fresh part of the morning. Rank lineages by suppression count, pick one with a long
history, plot each exclusion as a bar from its commit to the snapshot, annotate two or
three with what was excluded. Most bars should run to the right-hand edge — that is the
persistence finding made concrete.

**Then §3 Related work.** The 29-paper reading. The only remaining thing that could
still surprise you badly, and better found now than in review.

## Current headline numbers

| | |
|---|---|
| Ratchet | 5.4 : 1 (1,642 / 304) · 4.9 : 1 de-clustered |
| Invisible to structural diffing | 31% (503 of 1,642) |
| Persistence at 3 years | 86.7% (n = 1,584) · median undefined |
| Coverage-redundancy null | p = 0.49, n = 1,339 |
| Path exclusions enterable unprivileged | 64.1% · 33.0% need admin |
| Detector | precision 0.828 [0.711, 0.904] · recall 0.911 |

## Owed to people

- **Dacier** — corrected §5. Lead with §5.3: a third of path exclusions require
  privileged write, which concedes his point. Do not lead with 98.9%.
- **Elena Long** — confirm Tables 5 and 6 after the arXiv update (`git pull`; the
  `helper_fingerprint` change forces cache regeneration).

## Do not re-derive

Definitions live in `src/detector.py` and `src/forgeability.py`. Do not redefine them in
notebook cells — cell-local drift caused corrections 3 and 4.
