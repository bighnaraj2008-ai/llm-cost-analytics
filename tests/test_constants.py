import unittest
from src.constants import (
    DEFAULT_SPIKE_THRESHOLD,
    SUPPORTED_PROVIDERS,
    SUPPORTED_MODELS,
    VERSION
)

class TestConstants(unittest.TestCase):
    def test_default_threshold(self):
        self.assertEqual(DEFAULT_SPIKE_THRESHOLD, 10.0)

    def test_supported_providers(self):
        self.assertIn("openai", SUPPORTED_PROVIDERS)
        self.assertIn("anthropic", SUPPORTED_PROVIDERS)
        self.assertIn("google", SUPPORTED_PROVIDERS)

    def test_version_format(self):
        self.assertEqual(VERSION, "1.0.0")

if __name__ == "__main__":
    unittest.main()
