import unittest
import json
import os
from src.services.cost_calculator import CostCalculator

class TestCostCalculator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        fixture_path = os.path.join(os.path.dirname(__file__), "fixtures", "pricing_fixture.json")
        with open(fixture_path, "r", encoding="utf-8") as f:
            cls.pricing_fixtures = json.load(f)

    def test_calculate_cost_gpt4(self):
        # 200,000 prompt tokens * $0.03/1k = $6.00
        # 100,000 completion tokens * $0.06/1k = $6.00
        # Total = $12.00
        cost = CostCalculator.calculate_cost(200000, 100000, 0.03, 0.06)
        self.assertAlmostEqual(cost, 12.0, places=4)

    def test_calculate_cost_zero_tokens(self):
        cost = CostCalculator.calculate_cost(0, 0, 0.03, 0.06)
        self.assertEqual(cost, 0.0)

    def test_calculate_for_model_with_multiplier(self):
        # Base cost: (1000/1000)*0.0015 + (1000/1000)*0.002 = 0.0035
        # Multiplier 2.0 -> 0.007
        cost = CostCalculator.calculate_for_model(
            "gpt-3.5-turbo", 1000, 1000, self.pricing_fixtures, multiplier=2.0
        )
        self.assertAlmostEqual(cost, 0.007, places=4)

    def test_calculate_for_unknown_model_raises_key_error(self):
        with self.assertRaises(KeyError):
            CostCalculator.calculate_for_model(
                "unknown-model-xyz", 1000, 1000, self.pricing_fixtures
            )

if __name__ == "__main__":
    unittest.main()
