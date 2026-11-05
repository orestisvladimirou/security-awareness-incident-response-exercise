#!/usr/bin/env python3
"""Illustrate quiz scoring on invented profiles, not employees."""
import csv
from collections import defaultdict
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def load(path):
    with (ROOT/path).open(encoding='utf8',newline='') as f:
        return list(csv.DictReader(f))
def results():
    key={r['question_id']:r['correct_option'] for r in load('data/awareness_questions.csv')}
    points=defaultdict(int)
    for r in load('phase3/data/illustrative_training_responses.csv'):
        assert r['status']=='SYNTHETIC ANSWER KEY EXAMPLE - NOT EMPLOYEE TEST'
        assert r['correct_option']==key[r['question_id']]
        assert (r['is_correct']=='Yes')==(r['selected_option']==key[r['question_id']])
        points[r['model_id']]+=int(r['is_correct']=='Yes')
    return dict(sorted(points.items()))
if __name__=='__main__':
    print('SYNTHETIC MODEL ANSWERS ONLY — NO TRAINING WAS DELIVERED')
    for k,v in results().items():print(f'{k}: {v}/8 (model score only)')
