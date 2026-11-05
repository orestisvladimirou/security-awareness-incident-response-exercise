import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from validate_phase3 import check,p3
from score_training import results
class Phase3Tests(unittest.TestCase):
    def test_model_training_quality(self):self.assertTrue(check())
    def test_mock_results_not_people(self):
        self.assertEqual(results(),{'MODEL-CAUTIOUS':8,'MODEL-MIXED':6,'MODEL-NEEDS-COACHING':3})
        self.assertTrue(all(r['assurance']=='NOT A REAL PARTICIPANT OR TRAINING RESULT' for r in p3('illustrative_training_scorecards.csv')))
    def test_no_fake_closure(self):
        self.assertTrue(all(r['closure_decision']=='DO NOT CLOSE' for r in p3('action_effectiveness_gates.csv')))
