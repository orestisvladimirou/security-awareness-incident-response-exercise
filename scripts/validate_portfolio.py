#!/usr/bin/env python3
"""Verify final source-linked metrics, traceability, versioned simulation gates."""
import csv
from pathlib import Path
from validate_project import ROOT, load
from validate_phase3 import p3, check as phase3check
from validate_phase2 import p2
P4=ROOT/'phase4/data'
def p4(name):
    with (P4/name).open(encoding='utf8',newline='') as f:return list(csv.DictReader(f))
def check():
    phase3check()
    metrics=p4('portfolio_metrics.csv')
    trace=p4('incident_traceability.csv')
    assert len(metrics)==16 and len({r['metric_id'] for r in metrics})==16
    assert {r['metric_id'] for r in metrics}=={f'M{i:02d}' for i in range(1,17)}
    expected=[11,10,4,8,10,6,12,8,2,8,24,3,0,0,6,0]
    assert [int(r['value']) for r in metrics]==expected
    for r in metrics:
        assert (ROOT/r['source_path']).is_file(), f'Metric missing provenance: {r}'
        assert len(r['assurance_guard'])>=20
    injects={r['inject_id']:r for r in load('tabletop_injects.csv')}
    events={r['event_id']:r for r in load('scenario_events.csv')}
    evidence={r['evidence_id'] for r in load('evidence_register.csv')}
    decisions={r['decision_id'] for r in load('incident_decisions.csv')}
    actions={r['action_id'] for r in load('response_actions.csv')}
    assert len(trace)==6 and {r['inject_id'] for r in trace}==set(injects)
    for r in trace:
        assert r['first_evidence_id'] in injects[r['inject_id']]['evidence_ids'].split(';')
        assert r['first_evidence_id'] in evidence
        assert r['source_event'] in events
        assert r['first_evidence_id'] in events[r['source_event']]['source_evidence_ids'].split(';')
        assert r['decision_ref']==events[r['source_event']]['decision_ref'] in decisions
        assert r['response_action']==events[r['source_event']]['action_ref'] in actions
        assert r['safe_branch']=='A' and r['unsafe_branch']=='B'
        assert r['implementation_proof']=='NOT PROVIDED' and r['authorization']=='NONE - FICTIONAL'
    baseline=load('learning_metrics.csv')
    assert all(r['baseline_status']=='NOT MEASURED' and not r['scenario_value'] for r in baseline)
    assert all(r['authority_state']=='SIMULATED - NO SIGNOFF' for r in load('incident_decisions.csv'))
    assert all(r['status']=='OPEN - SIMULATED' for r in load('response_actions.csv'))
    print('PASS Phase 4: 16 source-linked metrics, 6 event/decision/action crosswalks and all unresolved assurance gates.')
    return True
if __name__=='__main__':check()
