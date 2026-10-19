import unittest
from datetime import datetime
from src.utils import format_currency, format_tokens, parse_date, format_table

class TestUtils(unittest.TestCase):
    def test_format_currency(self):
        self.assertEqual(format_currency(12.34567), "$12.3457")
        self.assertEqual(format_currency(0.001), "$0.0010")

    def test_format_tokens(self):
        self.assertEqual(format_tokens(300000), "300,000")
        self.assertEqual(format_tokens(5), "5")

    def test_parse_date(self):
        dt = parse_date("2026-10-19 10:00:00")
        self.assertIsNotNone(dt)
        self.assertEqual(dt.year, 2026)
        self.assertEqual(dt.month, 10)
        self.assertEqual(dt.day, 19)

    def test_parse_invalid_date(self):
        self.assertIsNone(parse_date("invalid-date-string"))

    def test_format_table(self):
        headers = ["Model", "Cost"]
        rows = [["gpt-4", "$12.00"], ["gpt-3.5", "$0.0035"]]
        table = format_table(headers, rows)
        self.assertIn("gpt-4", table)
        self.assertIn("Model", table)

if __name__ == "__main__":
    unittest.main()
