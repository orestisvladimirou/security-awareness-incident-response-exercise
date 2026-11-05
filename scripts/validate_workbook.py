#!/usr/bin/env python3
"""Read-only OOXML consistency validation for v0.1 snapshot. No third-party dependencies."""
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path
from validate_project import ROOT, load

N = '{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'
PATH = ROOT / 'Security_Awareness_Incident_Response_v0.1.xlsx'
EXPECTED = [
    'Dashboard', 'Incident Timeline', 'Evidence Register', 'Decision Log',
    'Response Actions', 'Tabletop Injects', 'Awareness Quiz', 'Learning Metrics'
]

def validate_workbook():
    assert PATH.is_file(), 'Companion workbook missing'
    with zipfile.ZipFile(PATH) as z:
        assert z.testzip() is None, 'Corrupted workbook'
        book = ET.fromstring(z.read('xl/workbook.xml'))
        names = [x.attrib['name'] for x in book.findall('.//' + N + 'sheet')]
        assert names == EXPECTED, f'Unexpected workbook sheets: {names}'
        root = ET.fromstring(z.read('xl/worksheets/sheet1.xml'))
        cells = {c.attrib['r']: c for c in root.findall('.//' + N + 'c')}
        actual_counts = [
            len(load('scenario_events.csv')),
            len(load('evidence_register.csv')),
            sum(x['confidence']=='Missing' for x in load('evidence_register.csv')),
            len(load('incident_decisions.csv')),
            sum(x['status']=='OPEN - SIMULATED' for x in load('response_actions.csv')),
            len(load('tabletop_injects.csv')),
            sum(x['state']=='RUN' for x in load('tabletop_injects.csv')),
            len(load('awareness_questions.csv')),
            sum(x['baseline_status']=='MEASURED' for x in load('learning_metrics.csv')),
        ]
        for i, expected in enumerate(actual_counts, 6):
            c = cells.get(f'B{i}')
            assert c is not None, f'Missing dashboard cell B{i}'
            f, v = c.find(N+'f'), c.find(N+'v')
            assert f is not None and v is not None and f.text, f'Missing formula/cache at B{i}'
            assert int(float(v.text)) == expected, f'B{i}: workbook cache {v.text} differs from CSV {expected}'
        assert 'COUNTIF' in cells['B8'].find(N+'f').text
        assert 'COUNTIF' in cells['B10'].find(N+'f').text
        for idx, fname in enumerate((
            'scenario_events.csv', 'evidence_register.csv', 'incident_decisions.csv',
            'response_actions.csv', 'tabletop_injects.csv', 'awareness_questions.csv',
            'learning_metrics.csv'
        ), start=2):
            sheet = ET.fromstring(z.read(f'xl/worksheets/sheet{idx}.xml'))
            r = sheet.findall('.//' + N + 'sheetData/' + N + 'row')
            assert len(r) == len(load(fname)) + 1, f'{names[idx-1]} row count mismatch'
    print('PASS workbook: 8 populated sheets, source record counts and cached formula KPIs match CSV.')
    return True

if __name__ == '__main__':
    validate_workbook()
