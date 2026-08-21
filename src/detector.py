r"""
Canonical definitions for suppression / relaxation detection over PGIR signatures.

Import these rather than redefining them in notebook cells — divergence between
the classifier's view and the worksheet's view invalidated one validation run.

    import sys; sys.path.insert(0, r'...\coverage-decay\src')
    from detector import *

Two conventions, both deliberate:

  * Predicates are counted DISTINCT. The same exclusion appearing in two branches
    of a condition tree is one exclusion, not two. 270 of 8,234 steps in the
    SigmaHQ corpus contain such duplicates.

  * A selection predicate whose only literal is '*' or '' adds no detection, so
    it cannot make a revision "expansion-with-guard". Ignoring it fixes a
    false-negative class found during hand validation (items V026, V091, V103,
    V104).
"""

import re

__all__ = ['norm', 'literals', 'neg_preds_fields', 'neg_set', 'pos_preds',
           'val_count', 'deltas', 'val_deltas', 'excl_size',
           'is_suppression', 'is_relaxation', 'is_expansion_with_guard',
           'real_pos_preds', 'stratum']

# a predicate ends at its CTX: marker; anything after is condition-tree syntax
# that varies with position and must not enter set comparisons
CUT = re.compile(r'^P:.*?CTX:(?:POS|NEG)', re.S)
LIT = re.compile(r"\('[A-Z]',")
LITVAL = re.compile(r"\('[A-Z]',\s*'([^']*)'\)")
TRIVIAL = re.compile(r"^P:[^|]+\|[A-Z]+\|\('[A-Z]',\s*'\*?'\)\|CTX:POS$")


def norm(v):
    """Collapse the multiple backslash-escaping layers in PGIR literals."""
    return re.sub(r'\\{2,}', r'\\', v)


def literals(pred):
    return LITVAL.findall(pred)


def _preds(sig):
    for frag in sig.split('P:')[1:]:
        m = CUT.match('P:' + frag.split('P:')[0])
        if m:
            yield m.group(0)


def neg_preds_fields(sig):
    """(field, predicate) for each DISTINCT negated predicate."""
    seen, out = set(), []
    for p in _preds(sig):
        if p.endswith('CTX:NEG') and p not in seen:
            seen.add(p)
            out.append((p[2:].split('|')[0], p))
    return out


def neg_set(sig):
    return {p for _, p in neg_preds_fields(sig)}


def pos_preds(sig):
    return {p for p in _preds(sig) if p.endswith('CTX:POS')}


def real_pos_preds(sig):
    """Selection predicates that actually constrain — catch-alls excluded."""
    return {p for p in pos_preds(sig) if not TRIVIAL.match(p)}


def val_count(sig, ctx):
    preds = neg_set(sig) if ctx == 'CTX:NEG' else pos_preds(sig)
    return sum(len(LIT.findall(p)) for p in preds)


def deltas(s):
    """(selection predicate delta, exclusion predicate delta) — distinct counts."""
    return (len(real_pos_preds(s['sig_b'])) - len(real_pos_preds(s['sig_a'])),
            len(neg_set(s['sig_b'])) - len(neg_set(s['sig_a'])))


def val_deltas(s):
    return (val_count(s['sig_b'], 'CTX:POS') - val_count(s['sig_a'], 'CTX:POS'),
            val_count(s['sig_b'], 'CTX:NEG') - val_count(s['sig_a'], 'CTX:NEG'))


def excl_size(sig):
    """Exclusion extent, for the survival restoration test."""
    return (len(neg_set(sig)), val_count(sig, 'CTX:NEG'))


def is_suppression(s):
    """Exclusion grew (predicate or value level); no new selection predicate."""
    dp, dn = deltas(s); vp, vn = val_deltas(s)
    return (dn > 0 or (dn == 0 and vn > 0)) and dp <= 0


def is_relaxation(s):
    """Mirror of is_suppression."""
    dp, dn = deltas(s); vp, vn = val_deltas(s)
    return (dn < 0 or (dn == 0 and vn < 0)) and dp >= 0


def is_expansion_with_guard(s):
    dp, dn = deltas(s); vp, vn = val_deltas(s)
    return (dn > 0 or (dn == 0 and vn > 0)) and dp > 0


def stratum(s):
    """Which negative bucket a non-suppression falls in (for validation sampling)."""
    if is_expansion_with_guard(s):                 return 'expansion-with-guard'
    if is_relaxation(s):                           return 'relaxation'
    if neg_set(s['sig_a']) != neg_set(s['sig_b']): return 'rewrite, no net change'
    return 'no exclusion change'
