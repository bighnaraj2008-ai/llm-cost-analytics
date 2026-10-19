import unittest
import os
from src.database import Database
from src.config import config
from src.services.analytics import AnalyticsService

class TestAnalytics(unittest.TestCase):
    def setUp(self):
        self.db = Database(":memory:")
        self.db.apply_migrations(config.migrations_dir)
        self.service = AnalyticsService(self.db)

    def tearDown(self):
        self.db.close()

    def test_daily_cost_per_user(self):
        results = self.service.get_daily_cost_per_user()
        self.assertTrue(len(results) > 0)
        user1_costs = [r["total_cost"] for r in results if r["user_id"] == "user1"]
        self.assertTrue(len(user1_costs) > 0)
        # user1 has request on 2026-10-19 with 200k prompt, 100k completion on gpt-4 -> $12.00
        self.assertTrue(any(cost >= 12.0 for cost in user1_costs))

    def test_model_utilization_breakdown(self):
        results = self.service.get_model_utilization()
        self.assertTrue(len(results) > 0)
        models = {r["model_name"] for r in results}
        self.assertIn("gpt-4", models)

    def test_cost_spike_detector(self):
        spikes = self.service.get_cost_spikes(threshold=10.0)
        self.assertTrue(len(spikes) >= 1)
        spike_users = [s["user_id"] for s in spikes]
        self.assertIn("user1", spike_users)
        for s in spikes:
            self.assertGreater(s["daily_spend"], 10.0)

    def test_token_trend_analysis(self):
        trends = self.service.get_token_trends()
        self.assertTrue(len(trends) > 0)
        self.assertIn("total_tokens", trends[0])
        self.assertIn("estimated_cost", trends[0])

if __name__ == "__main__":
    unittest.main()
