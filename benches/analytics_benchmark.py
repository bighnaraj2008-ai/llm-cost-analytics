"""Performance benchmarking harness for analytical aggregation workloads."""
import time
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.database import Database
from src.config import config
from src.services.analytics import AnalyticsService

def benchmark_queries():
    db = Database(":memory:")
    db.apply_migrations(config.migrations_dir)
    service = AnalyticsService(db)

    print("Running query execution benchmarks against SQLite memory instance...")

    t0 = time.perf_counter()
    for _ in range(100):
        service.get_daily_cost_per_user()
    t1 = time.perf_counter()
    print(f"Daily cost per user (100 runs): {((t1 - t0) / 100) * 1000:.3f} ms/run")

    t0 = time.perf_counter()
    for _ in range(100):
        service.get_model_utilization()
    t1 = time.perf_counter()
    print(f"Model utilization (100 runs): {((t1 - t0) / 100) * 1000:.3f} ms/run")

    t0 = time.perf_counter()
    for _ in range(100):
        service.get_cost_spikes(10.0)
    t1 = time.perf_counter()
    print(f"Cost spike detector (100 runs): {((t1 - t0) / 100) * 1000:.3f} ms/run")

if __name__ == "__main__":
    benchmark_queries()
