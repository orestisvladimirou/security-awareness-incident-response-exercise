#!/usr/bin/env python3
"""Standard-library integrity checks for an entirely fictional IR/awareness project."""
import csv
from datetime import datetime, timezone
from pathlib import Path
import re
import sys

ROOT=Path(__file__).resolve().parents[1]
CASE='IR-2026-001'
SIMULATION_DATE=datetime.fromisoformat('2026-11-05T00:00:00+00:00')

def load(name):
    with (ROOT/'data'/name).open(encoding='utf-8',newline='') as f:
        return list(csv.DictReader(f))

def unique(rows,key,n):
    values=[r[key] for r in rows]
    assert len(rows)==len(values)==len(set(values))==n, f'{key}: expected {n} unique entries'
    return set(values)

def when(value):
    dt=datetime.fromisoformat(value.replace('Z','+00:00'))
    assert dt.tzinfo is not None and dt.utcoffset().total_seconds()==0,'UTC is required'
    assert dt>SIMULATION_DATE, 'All scenario events must be future fictional events'
    return dt

def validate():
    events=load('scenario_events.csv')
    evidence=load('evidence_register.csv')
    decisions=load('incident_decisions.csv')
    actions=load('response_actions.csv')
    injects=load('tabletop_injects.csv')
    questions=load('awareness_questions.csv')
    metrics=load('learning_metrics.csv')
    roles=load('roles_raci.csv')
    ids_e=unique(events,'event_id',11)
    ids_ev=unique(evidence,'evidence_id',10)
    ids_d=unique(decisions,'decision_id',8)
    ids_a=unique(actions,'action_id',10)
    ids_i=unique(injects,'inject_id',6)
    ids_q=unique(questions,'question_id',8)
    unique(metrics,'metric_id',6)
    unique(roles,'activity',9)
    assert ids_e=={f'T-{i:03d}' for i in range(1,12)}
    assert ids_ev=={f'EV-{i:03d}' for i in range(1,11)}
    assert ids_d=={f'D-{i:03d}' for i in range(1,9)}
    assert ids_i=={f'INJ-{i:02d}' for i in range(1,7)}
    assert ids_q=={f'Q-{i:02d}' for i in range(1,9)}
    assert {a['decision_id'] for a in actions}==ids_d
    assert {e['case_id'] for e in events+evidence}=={CASE}
    statuses={e['confidence'] for e in events}
    assert 'Unknown-impact' in statuses and 'Missing' in statuses and 'Proposed-only' in statuses
    event_times=[when(e['scenario_timestamp_utc']) for e in events]
    assert event_times==sorted(event_times) and len(set(event_times))==len(event_times)
    assert when(events[0]['scenario_timestamp_utc']).strftime('%H:%M')=='08:40'
    for row in events:
        assert row['decision_ref'] in ids_d and row['action_ref'] in ids_a
        assert row['response_owner']
        assert all(eid in ids_ev for eid in row['source_evidence_ids'].split(';'))
        if row['event_type']=='Finding': assert 'read' in row['description'].lower()
    ev_map={e['evidence_id']:e for e in evidence}
    for row in evidence:
        when(row['scenario_timestamp_utc'])
        p=row['record_path']
        if p:
            f=ROOT/p
            assert f.is_file(), f'Missing synthetic evidence file: {p}'
            t=f.read_text(encoding='utf-8').upper()
            assert 'FICTIONAL' in t or 'SYNTHETIC' in t or 'FAKE' in t
            assert row['confidence']!='Missing'
        else:
            assert row['confidence']=='Missing' and row['preservation_status']=='MISSING - REQUESTED'
        assert row['limitation']
    assert {x for x in ids_ev if not ev_map[x]['record_path']}=={'EV-005','EV-007','EV-008','EV-009'}
    for row in decisions:
        assert row['authority_state']=='SIMULATED - NO SIGNOFF'
        when(row['decision_time_utc'])
        assert row['deciding_role'] and row['reversal_or_review_trigger']
        assert all(e in ids_ev for e in row['evidence_ids'].split(';'))
        assert 'propos' in row['provisional_direction'].lower() or row['decision_id'] in {'D-001','D-002','D-003','D-006','D-007','D-008'},'No unstated official decisions'
    for row in actions:
        assert row['status']=='OPEN - SIMULATED' and row['priority'] in ('P1','P2')
        when(row['target_scenario_utc'])
        assert row['phase'] in ('Detect','Analyze','Respond','Recover','Improve')
        assert row['verification_evidence']
        assert all(d in ids_a for d in row['dependency'].split(';') if d!='None')
        assert row['action_id'] not in row['dependency'].split(';')
    assert {row['phase'] for row in actions}=={'Detect','Analyze','Respond','Recover','Improve'}
    assert [int(i['minute']) for i in injects]==[0,12,25,40,55,70]
    for row in injects:
        assert row['state']=='NOT RUN - DESIGN ONLY' and row['success_criteria']
        assert all(e in ids_ev for e in row['evidence_ids'].split(';'))
        assert row['facilitator_prompt'] and row['expected_decision_topics']
    assert len({q['module_id'] for q in questions})==4
    for q in questions:
        assert q['correct_option'] in ('A','B','C') and q['rationale']
        assert all(q[k] for k in ('answer_a','answer_b','answer_c'))
    for m in metrics:
        assert m['baseline_status']=='NOT MEASURED' and not m['scenario_value']
        assert m['collection_method'] and m['owner_role'] and m['misinterpretation_guard']
    for row in roles:
        assert 'A' in ''.join(row[k] for k in ['incident_commander','soc','identity_admin','vendor_manager','privacy_lead','service_owner','awareness_lead'])
    missing_links=[]
    for md in ROOT.rglob('*.md'):
        for u in re.findall(r'\[[^\]]+\]\(([^)]+)\)',md.read_text(encoding='utf-8')):
            if u.startswith(('https://','http://','#','mailto:')): continue
            dest=u.split('#',1)[0]
            if dest and not (md.parent/dest).is_file():
                missing_links.append(f'{md.relative_to(ROOT)} -> {dest}')
    assert not missing_links, 'Broken links: '+'; '.join(missing_links)
    print('PASS: 11 timeline events, 10 evidence references (4 explicitly missing), 8 unsigned decisions, 10 open actions, 6 unrun tabletop injects, 8 training questions, 6 unmeasured metrics and local links.')
    return True

if __name__=='__main__':
    validate()
