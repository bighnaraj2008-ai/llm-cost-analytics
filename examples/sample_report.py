"""Runnable sample script demonstrating the programmatic analytics API."""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.database import Database
from src.config import config
from src.services.analytics import AnalyticsService

def main():
    # Use in-memory SQLite database populated with migrations
    db = Database(":memory:")
    db.apply_migrations(config.migrations_dir)

    service = AnalyticsService(db)
    daily = service.get_daily_cost_per_user()
    print(f"Successfully generated daily report with {len(daily)} user-date entries.")
    for entry in daily:
        print(f" -> User {entry['user_id']} incurred ${entry['total_cost']:.4f} across {entry['total_tokens']} tokens")

if __name__ == "__main__":
    main()
