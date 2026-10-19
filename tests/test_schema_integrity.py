import unittest
from src.database import Database
from src.config import config

class TestSchemaIntegrity(unittest.TestCase):
    def setUp(self):
        self.db = Database(":memory:")
        self.db.apply_migrations(config.migrations_dir)

    def tearDown(self):
        self.db.close()

    def test_sqlite_integrity_check(self):
        cursor = self.db.execute("PRAGMA integrity_check;")
        self.assertEqual(cursor.fetchone()[0], "ok")

    def test_foreign_key_check_clean(self):
        cursor = self.db.execute("PRAGMA foreign_key_check;")
        self.assertEqual(len(cursor.fetchall()), 0)

if __name__ == "__main__":
    unittest.main()
