#!/usr/bin/env python3
"""Check source snapshot hashes; not a proof of security or incident handling."""
import json, hashlib
from pathlib import Path
from validate_project import ROOT


def inventory():
    files = {}
    for p in ROOT.rglob('*'):
        if not p.is_file() or '__pycache__' in p.parts or '.git' in p.parts:
            continue
        if p.name=='SOURCE_MANIFEST.json' or p.suffix=='.pyc':
            continue
        data=p.read_bytes()
        files[p.relative_to(ROOT).as_posix()]={'sha256':hashlib.sha256(data).hexdigest(), 'bytes':len(data)}
    return files


def validate_manifest():
    data=json.loads((ROOT/'SOURCE_MANIFEST.json').read_text(encoding='utf-8'))
    assert data['version']=='0.4'
    actual=inventory()
    expected={r['path']:{'sha256':r['sha256'],'bytes':r['bytes']} for r in data['files']}
    assert actual==expected, 'Manifest stale or source file missing/changed. Regenerate deliberately.'
    print(f'PASS manifest: {len(actual)} recorded project files verified.')
    return True

if __name__=='__main__':
    validate_manifest()
