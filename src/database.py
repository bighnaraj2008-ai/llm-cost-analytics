import sqlite3
import os
from typing import Optional, List, Any

class Database:
    """SQLite database connection and migration manager."""

    def __init__(self, db_path: str = ":memory:"):
        self.db_path = db_path
        self.conn: Optional[sqlite3.Connection] = None

    def connect(self) -> sqlite3.Connection:
        if self.conn is None:
            self.conn = sqlite3.connect(self.db_path)
        return self.conn

    def execute(self, sql: str, params: tuple = ()) -> sqlite3.Cursor:
        conn = self.connect()
        return conn.execute(sql, params)

    def executemany(self, sql: str, seq_of_params: List[tuple]) -> sqlite3.Cursor:
        conn = self.connect()
        return conn.executemany(sql, seq_of_params)

    def executescript(self, sql_script: str) -> sqlite3.Cursor:
        conn = self.connect()
        return conn.executescript(sql_script)

    def commit(self):
        if self.conn:
            self.conn.commit()

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None

    def apply_migrations(self, migrations_dir: str):
        if not os.path.exists(migrations_dir):
            raise FileNotFoundError(f"Migrations directory '{migrations_dir}' not found")
        files = sorted(f for f in os.listdir(migrations_dir) if f.endswith(".sql"))
        for filename in files:
            filepath = os.path.join(migrations_dir, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                self.executescript(f.read())
        self.commit()
