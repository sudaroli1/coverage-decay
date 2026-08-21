r"""
Which attributes exclusions are written on, and whether an adversary can enter them.

Answers the objection that narrowing a rule need not cost coverage if the excluded
attribute is one an adversary cannot assume (M. Dacier, pers. comm., Aug 2026).

Two levels:

  classify(field)  -> attribute class. Mostly descriptive; 99% of exclusions land in
                      classes an adversary can influence, so this alone discriminates
                      little.

  anchor(value)    -> can the exclusion actually be entered, and at what cost. This is
                      the analysis that carries the claim. Restricted to path-valued
                      fields; content fields (CommandLine, ScriptBlockText, ...) are
                      forgeable by a different argument and reported separately.

Leading-wildcard values count as freely enterable: '*' derives from a Sigma
endswith/contains match, which is location-independent, so an exclusion on
'*\Windows\System32\csrss.exe' is satisfied by a file the adversary creates at
'C:\Users\<u>\tmp\Windows\System32\csrss.exe'. Values of the form '*C:\...' are
excluded from that reasoning — a drive letter cannot appear mid-path.

Usage:
    from detector import *
    from forgeability import report
    report(sup2)
"""

import csv
import pathlib
import re
from collections import Counter

from detector import neg_preds_fields, neg_set, literals, norm

CLASS_NAME = {1: 'process / file / registry content', 2: 'network identity',
              3: 'account identity', 4: 'system-assigned', 5: 'unclassified',
              6: 'operation parameters'}

PATTERNS = [
    (1, r'image|filename|commandline|originalfile|process(name|path)?$|company|product|'
        r'description|signature|imageloaded|currentdirectory|startfunction|scriptblock|'
        r'servicefilename|objectname|details|md5|sha\d|hash|_raw|parentfolder'),
    (2, r'destination|source(ip|hostname|port|address)|src_|dst_|queryname|dnsquery|'
        r'url|uri|http|remote|location|initiated$'),
    (3, r'user|account|member|subject(domain)?name|arn|principal|initiatedby|caller|'
        r'logonaccount'),
    (4, r'logonid|processid|processguid|eventid|threadid|guid|sequence|recordnumber|'
        r'providerguid|correlation'),
]

OVERRIDE = {
    'TargetObject': 1, 'ProcessNameBuffer': 1, 'ModifyingApplication': 1,
    'ApplicationPath': 1, 'Path': 1, 'CallTrace': 1, 'Application': 1,
    'HostApplication': 1, 'PipeName': 1, 'StartModule': 1, 'ParentCommand': 1,
    'Command': 1, 'Data': 1, 'Payload': 1, 'Device': 1, 'Signed': 1,
    'CertThumbprint': 1, 'ServiceName': 1, 'TaskName': 1, 'LocalName': 1,
    'Message': 1, 'ContextInfo': 1,
    'IpAddress': 2, 'id.orig_h': 2, 'id.resp_h': 2, 'id.resp_p': 2,
    'ServerAddress': 2, 'Address': 2, 'IpPort': 2, 'cs-referer': 2, 'r-dns': 2,
    'service': 2, 'Query': 2, 'query': 2, 'qtype_name': 2, 'answers': 2,
    'TargetServerName': 2, 'RelativeTargetName': 2,
    'AllowedToDelegateTo': 3, 'SidHistory': 3,
    'Provider_Name': 4, 'Provider': 4, 'Channel': 4, 'Level': 4, 'Task': 4,
    'ObjectType': 4, 'ObjectClass': 4, 'Feature_Name': 4, 'errorCode': 4,
    'errorMessage': 4, 'sc-status': 4, 'State': 4, 'Action': 4, 'rejected': 4,
    'Reason': 4, 'PossibleCause': 4, 'CreationUtcTime': 4, 'HostVersion': 4,
    'GrantedAccess': 6, 'GrantedAcces': 6, 'AccessMask': 6, 'AccessList': 6,
    'Protocol': 6, 'IntegrityLevel': 6, 'RequestedPolicy': 6, 'ValidatedPolicy': 6,
    'DataCondition': 6, 'FilterOrigin': 6, 'DeviceDetail.trusttype': 6,
    'param1': 6, 'responseElements': 6,
}

# fields whose values are filesystem paths, and for which anchor() is meaningful.
# Matched case-insensitively and with any Sigma modifier suffix stripped: the corpus
# contains TargetFilename/TargetFileName, OriginalFileName/OriginalFilename and
# 'ScriptBlockText:contains' as distinct field strings for the same field.
PATH_FIELDS = {'Image', 'ParentImage', 'SourceImage', 'TargetImage', 'SourceParentImage',
               'TargetParentImage', 'ChildImage', 'ImageName', 'ImagePath',
               'ImageFileName', 'TargetFilename', 'SourceFilename', 'ImageLoaded',
               'ProcessName', 'ParentProcessName', 'ApplicationPath',
               'ModifyingApplication', 'Path', 'ProcessNameBuffer', 'ServiceFileName',
               'CurrentDirectory', 'Application', 'HostApplication', 'OriginalFileName',
               'LocalName', 'Device'}
_PATH_LC = {f.lower() for f in PATH_FIELDS}


def base_field(field):
    """Strip a Sigma modifier suffix: 'ScriptBlockText:contains' -> 'ScriptBlockText'."""
    return field.split(':')[0]


def is_path_field(field):
    return base_field(field).lower() in _PATH_LC

ABS = re.compile(r'^\*?[a-z]:\\', re.I)
SYSROOT = re.compile(r'^\*?(\\systemroot\\|%systemroot%|%windir%|%programfiles)', re.I)
PROT = re.compile(r'^\*?([a-z]:)?\\?(windows|program files( \(x86\))?)\\', re.I)
USERW = re.compile(r'users\\|\\appdata\\|\\temp\\|\\tmp\\|\\downloads\\|\\public\\|'
                   r'%temp%|%appdata%|%localappdata%|%userprofile%', re.I)
REG = re.compile(r'\\registry\\|^hk(ey|lm|cu)', re.I)


def classify(field):
    field = base_field(field)
    if field in OVERRIDE:
        return OVERRIDE[field], CLASS_NAME[OVERRIDE[field]]
    f = field.lower()
    for cid, pat in PATTERNS:
        if re.search(pat, f):
            return cid, CLASS_NAME[cid]
    return 5, CLASS_NAME[5]


def anchor(v):
    v = norm(v).strip()
    if not v:            return 'empty'
    if REG.search(v):    return 'registry path'
    if USERW.search(v):  return 'user-writable path'
    if SYSROOT.match(v): return 'protected path'
    if ABS.match(v):     return 'protected path' if PROT.match(v) else 'other absolute path'
    if v.startswith('*') or '\\' not in v.rstrip('*'):
        return 'bare name or suffix'
    return 'other relative path'


def additions(suppressions):
    """(field, predicate) for each exclusion predicate added by each suppression."""
    for s in suppressions:
        before = neg_set(s['sig_a'])
        for field, pred in neg_preds_fields(s['sig_b']):
            if pred not in before:
                yield s, field, pred


def report(suppressions, results_dir=None):
    tally, rows = Counter(), []
    anc, content = Counter(), Counter()

    for s, field, pred in additions(suppressions):
        cid, name = classify(field)
        tally[(cid, name)] += 1
        rows.append({'lineage': s['lineage_id'], 'version_b': s['version_b'],
                     'field': field, 'class_id': cid, 'class': name})
        if cid == 1:
            if is_path_field(field):
                for v in literals(pred):
                    anc[anchor(v)] += 1
            else:
                content[base_field(field)] += len(literals(pred))

    total = sum(tally.values())
    print(f'field-additions across {len(suppressions)} suppressions: {total}\n')
    for (cid, name), n in sorted(tally.items()):
        print(f'{cid}  {name:<34} {n:>5}  {100*n/total:5.1f}%')
    infl = sum(n for (cid, _), n in tally.items() if cid in (1, 2, 3, 6))
    print(f'\nadversary-influenceable (1,2,3,6): {infl}  ({100*infl/total:.1f}%)')
    print(f'unclassified: {tally[(5, CLASS_NAME[5])]}')

    t = sum(anc.values())
    print(f'\nPATH-VALUED exclusion values: {t}\n')
    for k, n in anc.most_common():
        print(f'  {k:<24} {n:>5}  {100*n/t:5.1f}%')
    free = anc['bare name or suffix'] + anc['user-writable path']
    print(f'\nenterable without privilege: {free}  ({100*free/t:.1f}%)')
    print(f'requires privileged write  : {anc["protected path"]}  '
          f'({100*anc["protected path"]/t:.1f}%)')

    print(f'\nCONTENT-VALUED exclusions: {sum(content.values())}')
    for f, n in content.most_common(10):
        print(f'  {f:<24} {n}')

    if results_dir:
        p = pathlib.Path(results_dir) / 'field_classification.csv'
        with open(p, 'w', newline='', encoding='utf-8') as fh:
            w = csv.DictWriter(fh, fieldnames=['lineage', 'version_b', 'field',
                                               'class_id', 'class'])
            w.writeheader(); w.writerows(rows)
        print(f'\nwrote {p}')

    return tally, anc, content
