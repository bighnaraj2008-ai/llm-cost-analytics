"""Pre-flight smoke test verification script."""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.database import Database
from src.config import config
from src.services.analytics import AnalyticsService
from src.services.cost_calculator import CostCalculator

def run_smoke_test():
    print("Running pre-flight smoke tests...")
    # 1. Test database memory migration
    db = Database(":memory:")
    db.apply_migrations(config.migrations_dir)

    # 2. Test analytics service
    service = AnalyticsService(db)
    daily = service.get_daily_cost_per_user()
    assert len(daily) > 0, "Daily cost query returned 0 rows"

    # 3. Test cost calculation
    cost = CostCalculator.calculate_cost(1000, 1000, 0.0015, 0.002)
    assert abs(cost - 0.0035) < 1e-5, f"Cost calculation mismatch: {cost}"

    print("ALL SMOKE TESTS PASSED.")

if __name__ == "__main__":
    run_smoke_test()
