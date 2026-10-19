"""Utility script to export analytical query results to CSV."""
import sys
import os
import csv
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.database import Database
from src.config import config
from src.services.analytics import AnalyticsService

def export_daily_costs(output_path: str = "daily_costs_export.csv"):
    db = Database(config.db_path)
    db.apply_migrations(config.migrations_dir)
    service = AnalyticsService(db)

    results = service.get_daily_cost_per_user()
    if not results:
        print("No daily cost records to export.")
        return

    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(results[0].keys()))
        writer.writeheader()
        writer.writerows(results)

    print(f"Exported {len(results)} rows to {output_path}")

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "daily_costs_export.csv"
    export_daily_costs(out)
