#!/usr/bin/env python3
"""Validate tabletop decision branches and the explicitly unrun exercises."""
import csv
from collections import Counter, defaultdict
from pathlib import Path
from validate_project import ROOT, load, validate
from score_tabletop import results as model_results
P2=ROOT/'phase2/data'
def p2(name):
    with (P2/name).open(encoding='utf8',newline='') as f:return list(csv.DictReader(f))
def check():
    validate()
    ids={r['inject_id'] for r in load('tabletop_injects.csv')}
    evid={r['evidence_id'] for r in load('evidence_register.csv')}
    branches=p2('decision_branches.csv');challenges=p2('evidence_challenges.csv');rubric=p2('scoring_rubric.csv');examples=p2('illustrative_tabletop_answers.csv')
    assert len(ids)==6 and len(branches)==12 and len(challenges)==8 and len(rubric)==6 and len(examples)==12
    keys={(r['inject_id'],r['option']) for r in branches}
    assert len(keys)==12 and keys=={(i,o) for i in ids for o in ('A','B')}
    assert Counter(r['model_points'] for r in branches)=={'2':6,'0':6}
    for r in branches:
        assert r['evidence_ids'] and r['basis_or_gap'] and len(r['failure_guard'])>=30
        assert all(x in evid for x in r['evidence_ids'].split(';'))
    assert len({r['case_id'] for r in challenges})==8
    for r in challenges:
        assert r['inject_id'] in ids and r['evidence_id'] in evid and r['decision_limit']
    assert {r['inject_id'] for r in rubric}==ids
    assert all(r['max_points']=='2' and r['delivery_state']=='NOT ADMINISTERED' for r in rubric)
    assert {r['model_id'] for r in examples}=={'MODEL-EVIDENCE-LED','MODEL-RUSHED'}
    assert model_results()=={'MODEL-EVIDENCE-LED':12,'MODEL-RUSHED':2}
    assert all(r['delivery_status']=='WORKED EXAMPLE - NO PARTICIPANTS' for r in examples)
    print('PASS Phase 2: 12 safe/unsafe paths, 8 evidence questions, 6 unadministered rubric criteria; 2 worked model profiles, no participants.')
    return True
if __name__=='__main__':check()
