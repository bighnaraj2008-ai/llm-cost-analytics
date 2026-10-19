import unittest
import os
import csv
from src.database import Database
from src.config import config
from src.services.analytics import AnalyticsService
from src.cli import handle_export

class TestExport(unittest.TestCase):
    def setUp(self):
        self.db = Database(":memory:")
        self.db.apply_migrations(config.migrations_dir)
        self.service = AnalyticsService(self.db)
        self.temp_csv = "temp_test_export.csv"

    def tearDown(self):
        self.db.close()
        if os.path.exists(self.temp_csv):
            os.remove(self.temp_csv)

    def test_handle_export_creates_valid_csv(self):
        handle_export(self.service, self.temp_csv)
        self.assertTrue(os.path.exists(self.temp_csv))
        with open(self.temp_csv, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            rows = list(reader)
            self.assertTrue(len(rows) > 1)
            headers = rows[0]
            self.assertIn("user_id", headers)
            self.assertIn("total_cost", headers)

if __name__ == "__main__":
    unittest.main()
