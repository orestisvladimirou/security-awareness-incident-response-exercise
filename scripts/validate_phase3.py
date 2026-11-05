#!/usr/bin/env python3
"""Validate synthetic learning examples, open closure gates and lesson links."""
import csv
from collections import Counter
from validate_phase2 import ROOT, p2, check as phase2check
from validate_project import load
from score_training import results as training_results
P3=ROOT/'phase3/data'
def p3(name):
    with (P3/name).open(encoding='utf8',newline='') as f:return list(csv.DictReader(f))
def check():
    phase2check()
    key={r['question_id']:r for r in load('awareness_questions.csv')}
    actions={r['action_id']:r for r in load('response_actions.csv')}
    responses=p3('illustrative_training_responses.csv')
    scorecards=p3('illustrative_training_scorecards.csv')
    feedback=p3('learning_feedback_map.csv')
    rollout=p3('awareness_rollout_plan.csv')
    followup=p3('action_effectiveness_gates.csv')
    lessons=p3('lessons_tracker.csv')
    assert len(responses)==24 and len(scorecards)==3 and len(feedback)==8 and len(rollout)==4 and len(followup)==10 and len(lessons)==6
    assert len({(r['model_id'],r['question_id']) for r in responses})==24
    assert all(r['question_id'] in key and r['correct_option']==key[r['question_id']]['correct_option'] for r in responses)
    assert all(r['status']=='SYNTHETIC ANSWER KEY EXAMPLE - NOT EMPLOYEE TEST' for r in responses)
    assert training_results()=={'MODEL-CAUTIOUS':8,'MODEL-MIXED':6,'MODEL-NEEDS-COACHING':3}
    assert {r['model_id']:int(r['correct_count']) for r in scorecards}==training_results()
    assert all(r['assurance']=='NOT A REAL PARTICIPANT OR TRAINING RESULT' for r in scorecards)
    assert {r['question_id'] for r in feedback}==set(key)
    assert all(r['safe_option']==key[r['question_id']]['correct_option'] for r in feedback)
    assert {r['module_id'] for r in rollout}=={r['module_id'] for r in key.values()}
    assert all(r['approval_state']=='NOT APPROVED OR DELIVERED' for r in rollout)
    assert {r['action_id'] for r in followup}==set(actions)
    assert all(r['prior_state']==actions[r['action_id']]['status']=='OPEN - SIMULATED' for r in followup)
    assert all(r['followup_state']=='OPEN - NO OPERATIONAL EVIDENCE' and r['closure_decision']=='DO NOT CLOSE' and r['approval_status']=='NOT OBTAINED' and r['independent_review']=='NOT CONDUCTED' for r in followup)
    assert {r['lesson_id'] for r in lessons}=={f'LL-{i:02d}' for i in range(1,7)}
    assert all(r['status']=='OPEN - SCENARIO' and all(x in actions for x in r['linked_actions'].split(';')) for r in lessons)
    assert all(r['baseline_status']=='NOT MEASURED' and r['scenario_value']=='' for r in load('learning_metrics.csv'))
    print('PASS Phase 3: 24 model answers, 3 artificial scorecards, 4 undelivered modules, 10 open corrective actions, 6 open lessons; no real trainees.')
    return True
if __name__=='__main__':check()
