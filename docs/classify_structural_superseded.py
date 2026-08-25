import pickle, re
from collections import Counter

so  = pickle.load(open('analysis/scripts/.cache/struct_ops_sigma.pkl','rb'))
res = so['results']

def root_op(sig):
    m = re.match(r"\(\\?'O:(\w+)", sig)
    return m.group(1) if m else 'other'

def has_neg(r):
    return 'CTX:NEG' in r['sig_a'] or 'CTX:NEG' in r['sig_b']

def direction(r):
    e, o = r['evidence'], r['ops']
    ra = root_op(r['sig_a'])
    narrow = broaden = 0

    narrow  += e['n_pred_added_under_existing_and']
    narrow  += e['n_pred_removed_from_existing_or']
    broaden += e['n_pred_removed_from_existing_and']
    broaden += e['n_pred_added_under_existing_or']

    if ra == 'AND':
        narrow  += e['n_pred_added_at_root']
        broaden += e['n_pred_removed_at_root']
    elif ra == 'OR':
        broaden += e['n_pred_added_at_root']
        narrow  += e['n_pred_removed_at_root']

    if o['BRANCH_AND_ADD']:    narrow  += 1
    if o['BRANCH_OR_REMOVE']:  narrow  += 1
    if o['BRANCH_AND_REMOVE']: broaden += 1
    if o['BRANCH_OR_ADD']:     broaden += 1

    if e['n_new_not_ops']:     narrow  += e['n_new_not_ops']
    if e['n_removed_not_ops']: broaden += e['n_removed_not_ops']

    if narrow and not broaden: return 'narrow'
    if broaden and not narrow: return 'broaden'
    if narrow and broaden:     return 'mixed'
    return 'unclassified'

pure  = [r for r in res if not has_neg(r)]
withn = [r for r in res if has_neg(r)]
print(f'total steps            : {len(res)}')
print(f'  purely positive logic: {len(pure)}')
print(f'  involve a negation   : {len(withn)}')
print()
print('PURE-POSITIVE steps:', Counter(direction(r) for r in pure).most_common())
print('NEGATION steps     :', Counter(direction(r) for r in withn).most_common())

# ---- intersect narrowing events with singleton-covered techniques ----
import json
from collections import Counter, defaultdict

tags  = json.load(open('lineage_attack_tags.json'))
study = {r['lineage_id'] for r in res}

def techs(lid):
    return [t for t in tags.get(lid, []) if t.split('.')[1:2] and t.split('.')[1].startswith('t')]

cover = Counter(t for l in study for t in techs(l))
singletons = {t for t, n in cover.items() if n == 1}

narrow_pure = [r for r in pure if direction(r) == 'narrow']
print()
print(f'pure-positive narrowing steps      : {len(narrow_pure)}')
print(f'  on lineages carrying tags        : {sum(1 for r in narrow_pure if techs(r["lineage_id"]))}')

hit = defaultdict(list)
for r in narrow_pure:
    for t in techs(r['lineage_id']):
        if t in singletons:
            hit[t].append(r['lineage_id'])

print(f'singleton techniques (total)       : {len(singletons)}')
print(f'  whose ONE rule was narrowed      : {len(hit)}')
print(f'  narrowing events on those rules  : {sum(len(v) for v in hit.values())}')
print()
print('techniques whose only rule was narrowed:')
for t, v in sorted(hit.items(), key=lambda x: -len(x[1]))[:15]:
    print(f'   {t:24} {len(v)} narrowing step(s)')
