"""Helper script to run all analytics reports sequentially."""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.database import Database
from src.config import config
from src.services.analytics import AnalyticsService

def main():
    db = Database(config.db_path)
    db.apply_migrations(config.migrations_dir)
    service = AnalyticsService(db)

    print("=== DAILY COST PER USER ===")
    for row in service.get_daily_cost_per_user():
        print(f"User: {row['user_id']:<10} Date: {row['usage_date']} Cost: ${row['total_cost']:.4f} Tokens: {row['total_tokens']}")

    print("\n=== MODEL UTILIZATION BREAKDOWN ===")
    for row in service.get_model_utilization():
        print(f"Model: {row['model_name']:<18} Requests: {row['request_count']:<6} Tokens: {row['total_tokens']:<8} Cost: ${row['total_cost']:.4f}")

    print("\n=== COST SPIKES (> $10.00) ===")
    for row in service.get_cost_spikes(10.0):
        print(f"ALERT: User {row['user_id']} spent ${row['daily_spend']:.4f} on {row['usage_date']}")

if __name__ == "__main__":
    main()
