import unittest
import sqlite3
import os
from src.database import Database
from src.config import config

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db = Database(":memory:")
        self.db.apply_migrations(config.migrations_dir)

    def tearDown(self):
        self.db.close()

    def test_schema_tables_exist(self):
        cursor = self.db.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = {row["name"] for row in cursor.fetchall()}
        self.assertIn("model_pricing", tables)
        self.assertIn("api_requests", tables)

    def test_foreign_key_enforcement(self):
        # Attempting to insert an api_request with non-existent model_id must fail
        with self.assertRaises(sqlite3.IntegrityError):
            self.db.execute(
                "INSERT INTO api_requests (user_id, model_id, prompt_tokens, completion_tokens, total_tokens) VALUES ('u99', 9999, 10, 10, 20);"
            )

    def test_indexes_exist(self):
        cursor = self.db.execute("SELECT name FROM sqlite_master WHERE type='index';")
        indexes = {row["name"] for row in cursor.fetchall()}
        self.assertIn("idx_api_requests_user_id", indexes)
        self.assertIn("idx_api_requests_model_id", indexes)

if __name__ == "__main__":
    unittest.main()
