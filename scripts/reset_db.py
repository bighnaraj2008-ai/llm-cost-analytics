"""Helper script to reset and seed the analytics database."""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.config import config
from src.database import Database

def main():
    if os.path.exists(config.db_path):
        os.remove(config.db_path)
        print(f"Removed database at {config.db_path}")

    db = Database(config.db_path)
    db.apply_migrations(config.migrations_dir)
    db.close()
    print("Database freshly initialized and seeded.")

if __name__ == "__main__":
    main()
