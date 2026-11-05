import sys, unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from validate_project import validate,load

class IncidentResponsePortfolioTests(unittest.TestCase):
    def test_complete_integrity(self):
        self.assertTrue(validate())
    def test_observation_does_not_claim_exfiltration(self):
        readings=[x for x in load('scenario_events.csv') if x['event_type']=='Finding']
        self.assertEqual(len(readings),1)
        self.assertEqual(readings[0]['source_evidence_ids'],'EV-003')
        notes=Path(__file__).resolve().parents[1]/'evidence/EV-003-ticket-audit.md'
        self.assertIn('not** proof of an export',notes.read_text(encoding='utf-8').lower())
    def test_sensitive_evidence_missing(self):
        unknown={r['evidence_id'] for r in load('evidence_register.csv') if r['confidence']=='Missing'}
        self.assertEqual(unknown,{'EV-005','EV-007','EV-008','EV-009'})
    def test_not_a_performed_exercise(self):
        self.assertTrue(all(r['state']=='NOT RUN - DESIGN ONLY' for r in load('tabletop_injects.csv')))
        self.assertTrue(all(r['status']=='OPEN - SIMULATED' for r in load('response_actions.csv')))
    def test_no_staff_results_invented(self):
        self.assertTrue(all(r['baseline_status']=='NOT MEASURED' and not r['scenario_value'] for r in load('learning_metrics.csv')))
    def test_decisions_have_no_signatures(self):
        self.assertTrue(all(r['authority_state']=='SIMULATED - NO SIGNOFF' for r in load('incident_decisions.csv')))
    def test_question_bank_consistent(self):
        questions=load('awareness_questions.csv')
        self.assertEqual(len(questions),8)
        self.assertEqual({x['module_id'] for x in questions},{'M-01','M-02','M-03','M-04'})

if __name__=='__main__':unittest.main()
