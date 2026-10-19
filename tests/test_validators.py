import unittest
from src.validators import (
    validate_token_count,
    validate_cost_rate,
    validate_user_id,
    validate_pricing_tier,
    ValidationError
)

class TestValidators(unittest.TestCase):
    def test_valid_tokens(self):
        self.assertEqual(validate_token_count(100), 100)
        self.assertEqual(validate_token_count(0), 0)

    def test_invalid_tokens_raises(self):
        with self.assertRaises(ValidationError):
            validate_token_count(-5)

    def test_valid_cost_rate(self):
        self.assertEqual(validate_cost_rate(0.03), 0.03)

    def test_invalid_cost_rate_raises(self):
        with self.assertRaises(ValidationError):
            validate_cost_rate(-0.01)

    def test_valid_user_id(self):
        self.assertEqual(validate_user_id("user123"), "user123")

    def test_invalid_user_id_raises(self):
        with self.assertRaises(ValidationError):
            validate_user_id("   ")

    def test_valid_pricing_tier(self):
        data = {
            "model_name": "gpt-4",
            "input_cost_per_1k_tokens": 0.03,
            "output_cost_per_1k_tokens": 0.06
        }
        self.assertEqual(validate_pricing_tier(data), data)

    def test_missing_pricing_tier_field_raises(self):
        with self.assertRaises(ValidationError):
            validate_pricing_tier({"model_name": "gpt-4"})

if __name__ == "__main__":
    unittest.main()
