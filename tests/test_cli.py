import unittest
from src.cli import create_parser

class TestCLI(unittest.TestCase):
    def setUp(self):
        self.parser = create_parser()

    def test_migrate_command_parsing(self):
        args = self.parser.parse_args(["migrate"])
        self.assertEqual(args.command, "migrate")

    def test_seed_command_parsing(self):
        args = self.parser.parse_args(["seed"])
        self.assertEqual(args.command, "seed")

    def test_report_command_parsing_defaults(self):
        args = self.parser.parse_args(["report"])
        self.assertEqual(args.command, "report")
        self.assertEqual(args.type, "daily")
        self.assertEqual(args.threshold, 10.0)

    def test_report_command_custom_args(self):
        args = self.parser.parse_args(["report", "--type", "spikes", "--threshold", "25.5"])
        self.assertEqual(args.type, "spikes")
        self.assertEqual(args.threshold, 25.5)

    def test_export_command_parsing(self):
        args = self.parser.parse_args(["export", "-o", "custom_out.csv"])
        self.assertEqual(args.command, "export")
        self.assertEqual(args.output, "custom_out.csv")

if __name__ == "__main__":
    unittest.main()
