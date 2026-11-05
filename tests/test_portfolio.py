import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from validate_portfolio import check,p4
class FinalQualityTests(unittest.TestCase):
    def test_integrity(self):self.assertTrue(check())
    def test_provenance_links(self):
        root=Path(__file__).resolve().parents[1]
        self.assertTrue(all((root/r['source_path']).is_file() for r in p4('portfolio_metrics.csv')))
    def test_assurance_boundaries(self):
        dashboard=(Path(__file__).resolve().parents[1]/'phase4/dashboard.md').read_text(encoding='utf8')
        self.assertIn('NO INCIDENT',dashboard)
        self.assertIn('NOT REAL',dashboard.upper())
        self.assertIn('NOT MEASURED',dashboard.upper()) if 'NOT MEASURED' in dashboard.upper() else self.assertIn('zero measured baselines',dashboard.lower())
