import sys, unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from validate_workbook import validate_workbook
from validate_manifest import validate_manifest

class DeliveryQualityTests(unittest.TestCase):
    def test_workbook_matches_csv(self):
        self.assertTrue(validate_workbook())

    def test_file_manifest(self):
        self.assertTrue(validate_manifest())

if __name__=='__main__':unittest.main()
