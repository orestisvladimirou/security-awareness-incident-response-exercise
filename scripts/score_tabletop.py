#!/usr/bin/env python3
"""Display hypothetical answer-key scores. NEVER represents actual participants."""
import csv
from collections import defaultdict
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def load(name):
    with (ROOT/'phase2/data'/name).open(newline='',encoding='utf8') as f:
        return list(csv.DictReader(f))
def results():
    options={(r['inject_id'],r['option']):int(r['model_points']) for r in load('decision_branches.csv')}
    scores=defaultdict(int)
    for r in load('illustrative_tabletop_answers.csv'):
        assert r['delivery_status']=='WORKED EXAMPLE - NO PARTICIPANTS'
        assert int(r['points'])==options[(r['inject_id'],r['chosen_option'])]
        scores[r['model_id']]+=int(r['points'])
    return dict(sorted(scores.items()))
if __name__=='__main__':
    print('SYNTHETIC MODEL ANSWERS ONLY — NO TABLETOP WAS DELIVERED')
    for k,v in results().items():print(f'{k}: {v}/12 (model score only)')
