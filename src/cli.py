import argparse

def create_parser() -> argparse.ArgumentParser:
    """Define CLI commands for running analytics reports."""
    parser = argparse.ArgumentParser(
        prog="llm-cost-analytics",
        description="LLM Cost Analytics & Aggregation Engine"
    )
    subparsers = parser.add_subparsers(dest="command", help="Available subcommands")

    subparsers.add_parser("migrate", help="Run database schema migrations")
    subparsers.add_parser("seed", help="Seed default model pricing and sample usage telemetry")

    report_parser = subparsers.add_parser("report", help="Run analytics reports")
    report_parser.add_argument(
        "--type",
        choices=["daily", "models", "spikes", "trends"],
        default="daily",
        help="Report type to generate"
    )
    report_parser.add_argument(
        "--threshold",
        type=float,
        default=10.0,
        help="Spend threshold for spike detection"
    )

    export_parser = subparsers.add_parser("export", help="Export analytics to CSV")
    export_parser.add_argument("--output", "-o", default="daily_costs.csv", help="Output CSV path")

    return parser
