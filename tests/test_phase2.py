import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from validate_phase2 import check,p2
from score_tabletop import results
class Phase2Tests(unittest.TestCase):
    def test_branches_and_challenges(self):self.assertTrue(check())
    def test_model_scores_are_only_examples(self):
        self.assertEqual(results(),{'MODEL-EVIDENCE-LED':12,'MODEL-RUSHED':2})
        self.assertTrue(all(r['delivery_status']=='WORKED EXAMPLE - NO PARTICIPANTS' for r in p2('illustrative_tabletop_answers.csv')))
    def test_unrun_rubric(self):self.assertTrue(all(r['delivery_state']=='NOT ADMINISTERED' for r in p2('scoring_rubric.csv')))
