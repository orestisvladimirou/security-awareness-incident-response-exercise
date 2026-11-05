#!/usr/bin/env python3
"""Intentionally regenerate source checksum record after a controlled update."""
import json
from validate_project import ROOT
from validate_manifest import inventory

def main():
    files=inventory()
    obj={
       'project':'Security-Awareness-Incident-Response-Exercise',
       'version':'0.4',
       'created_on':'2026-11-05',
       'assurance':'Entirely fictional; no actual tabletop or training delivered',
       'files':[{'path':name, **vals} for name, vals in sorted(files.items())],
    }
    (ROOT/'SOURCE_MANIFEST.json').write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(f'Updated manifest for {len(files)} project files')

if __name__=='__main__':main()
