"""
Map rule lineages to MITRE ATT&CK techniques.

Sigma rules carry a stable UUID in their `id` field, which survives renames and moves.
The upstream lineage metadata records every UUID a lineage has held, so we index the
SigmaHQ working tree by UUID and join on that rather than on file path.
"""
import json, os, glob
from pathlib import Path

import yaml

SIGMA    = Path('../sigma')
METADATA = Path('../Evolution-of-Log-Based-Detection-Rules/'
                'data_prep/build_data/lineage_metadata_final_sigma.json')
OUT      = Path('results/lineage_attack_tags.json')


def index_rules_by_uuid():
    index = {}
    for path in glob.glob(str(SIGMA / 'rules*/**/*.yml'), recursive=True):
        try:
            with open(path, encoding='utf-8') as fh:
                doc = yaml.safe_load(fh)
        except Exception:
            continue
        if not isinstance(doc, dict) or not doc.get('id'):
            continue
        index[doc['id']] = [t for t in (doc.get('tags') or [])
                            if str(t).startswith('attack.')]
    return index


def main():
    uuid_tags = index_rules_by_uuid()
    print(f'rules indexed by UUID : {len(uuid_tags)}')

    lineages = json.load(METADATA.open())
    print(f'lineages in metadata  : {len(lineages)}')

    out = {}
    for lineage in lineages:
        tags = sorted({t for rid in (lineage.get('all_ids') or [])
                       for t in uuid_tags.get(rid, [])})
        out[lineage['lineage_id']] = tags

    tagged = sum(1 for v in out.values() if v)
    print(f'lineages with tags    : {tagged}  ({100*tagged/len(out):.1f}%)')

    OUT.parent.mkdir(exist_ok=True)
    json.dump(out, OUT.open('w'), indent=1)
    print(f'written: {OUT}')


if __name__ == '__main__':
    main()
