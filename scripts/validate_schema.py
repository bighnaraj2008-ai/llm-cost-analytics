"""Database schema integrity validator script."""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.database import Database
from src.config import config

def validate_schema():
    db = Database(config.db_path)
    db.apply_migrations(config.migrations_dir)

    # Run SQLite integrity check
    cursor = db.execute("PRAGMA integrity_check;")
    result = cursor.fetchone()[0]
    if result != "ok":
        raise RuntimeError(f"Database integrity check failed: {result}")

    # Check foreign keys pragma
    cursor = db.execute("PRAGMA foreign_key_check;")
    violations = cursor.fetchall()
    if violations:
        raise RuntimeError(f"Foreign key violations found: {violations}")

    print("Database schema integrity: PASS (0 violations, PRAGMA ok)")

if __name__ == "__main__":
    validate_schema()
