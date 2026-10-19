"""Simulation script demonstrating automated cost spike alerting."""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.database import Database
from src.config import config
from src.services.analytics import AnalyticsService

def simulate_alert_pipeline():
    db = Database(":memory:")
    db.apply_migrations(config.migrations_dir)
    service = AnalyticsService(db)

    print("Simulating real-time cost spike monitoring monitor...")
    spikes = service.get_cost_spikes(threshold=10.0)

    for spike in spikes:
        print(f"[ALERT TRIGGERED] User '{spike['user_id']}' exceeded daily threshold!")
        print(f" -> Date: {spike['usage_date']}")
        print(f" -> Daily Spend: ${spike['daily_spend']:.2f}")
        print(f" -> Total Tokens: {spike['total_tokens']:,}")

if __name__ == "__main__":
    simulate_alert_pipeline()
