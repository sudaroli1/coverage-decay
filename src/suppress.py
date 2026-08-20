"""
Suppression detection and exposure measurement.

A detection rule suppresses false positives by growing its exclusion set. In Sigma this
is expressed as a negation: `condition: selection and not filter`. We therefore detect
suppression semantically rather than structurally — a revision in which the number of
predicates in negated context increases is an exclusion growing, which narrows detection.

This replaces an earlier structural classifier. See docs/ for why that approach failed.

Run from the repository root, with the Evolution-of-Log-Based-Detection-Rules checkout
and the SigmaHQ clone as siblings. See data/README.md.
"""
import json, pickle, sys
from collections import Counter, defaultdict
from pathlib import Path

import pandas as pd

UPSTREAM = Path('../Evolution-of-Log-Based-Detection-Rules')
CACHE    = UPSTREAM / 'analysis/scripts/.cache/struct_ops_sigma.pkl'
PGIR     = UPSTREAM / 'data_prep/ir_data/pgir_sigma_nonempty.jsonl'
TAGS     = Path('results/lineage_attack_tags.json')
SNAPSHOT = pd.Timestamp('2026-04-10', tz='UTC')


def negated_predicates(sig: str) -> int:
    """Count predicates sitting inside a negation. Each predicate in the signature
    carries its own context marker, so this needs no tree parsing."""
    return sig.count('CTX:NEG')


def is_suppression(step) -> bool:
    """True when the exclusion set grew — detection narrowed."""
    return negated_predicates(step['sig_b']) > negated_predicates(step['sig_a'])


def is_relaxation(step) -> bool:
    return negated_predicates(step['sig_b']) < negated_predicates(step['sig_a'])


def techniques(tags, lineage_id):
    return [t for t in tags.get(lineage_id, [])
            if t.split('.')[1:2] and t.split('.')[1].startswith('t')]


def load_commit_dates(lineage_ids):
    """lineage_id, version_index -> commit timestamp."""
    dates = {}
    with PGIR.open(encoding='utf-8') as fh:
        for line in fh:
            if not line.strip():
                continue
            rec = json.loads(line)
            if rec['lineage_id'] in lineage_ids:
                dates[(rec['lineage_id'], rec['version_index'])] = \
                    pd.to_datetime(rec['commit_date'], utc=True)
    return dates


def main():
    steps = pickle.load(CACHE.open('rb'))['results']
    tags  = json.load(TAGS.open())

    suppressions = [s for s in steps if is_suppression(s)]
    relaxations  = [s for s in steps if is_relaxation(s)]

    print(f'steps                          : {len(steps):>6}')
    print(f'  suppressions (exclusion grew): {len(suppressions):>6}')
    print(f'  relaxations  (shrank)        : {len(relaxations):>6}')
    print(f'  ratchet ratio                : {len(suppressions)/max(len(relaxations),1):.1f} : 1')

    study    = {s['lineage_id'] for s in steps}
    coverage = Counter(t for l in study for t in techniques(tags, l))
    singleton = {t for t, n in coverage.items() if n == 1}

    print(f'\ntechniques covered             : {len(coverage):>6}')
    print(f'  by exactly one rule          : {len(singleton):>6}')

    affected = defaultdict(list)
    for s in suppressions:
        for t in techniques(tags, s['lineage_id']):
            if t in singleton:
                affected[t].append(s)

    events = [s for v in affected.values() for s in v]
    print(f'\nsingleton techniques suppressed: {len(affected):>6}')
    print(f'  suppression events           : {len(events):>6}')

    by_lineage = defaultdict(list)
    for s in steps:
        by_lineage[s['lineage_id']].append(s)
    for v in by_lineage.values():
        v.sort(key=lambda x: x['version_a'])

    dates = load_commit_dates({s['lineage_id'] for s in events})

    rows = []
    for technique, evs in affected.items():
        for s in evs:
            lid   = s['lineage_id']
            before = negated_predicates(s['sig_a'])
            t0 = dates.get((lid, s['version_b']))
            if t0 is None:
                continue
            after = [x for x in by_lineage[lid] if x['version_a'] >= s['version_b']]
            undone = next((x for x in after
                           if negated_predicates(x['sig_b']) <= before), None)
            if undone is not None:
                t1 = dates.get((lid, undone['version_b']))
                if t1 is None:
                    continue
                duration, censored = (t1 - t0).total_seconds() / 86400.0, False
            else:
                duration, censored = (SNAPSHOT - t0).total_seconds() / 86400.0, True
            rows.append({'technique': technique, 'lineage': lid,
                         'suppressed_on': t0.date(), 'days': round(duration, 1),
                         'censored': censored})

    df = pd.DataFrame(rows).sort_values('days', ascending=False)
    df.to_csv('results/singleton_suppression_exposure.csv', index=False)

    print(f'\n  never removed                : {df.censored.sum():>6}'
          f'   ({100*df.censored.mean():.1f}%)')
    print(f'  median days, never removed   : {df.loc[df.censored, "days"].median():>6.0f}')
    print(f'  median days, removed         : {df.loc[~df.censored, "days"].median():>6.1f}')
    print('\nwritten: results/singleton_suppression_exposure.csv')


if __name__ == '__main__':
    main()
