import argparse
import sys
import csv
from src.database import Database
from src.config import config
from src.services.analytics import AnalyticsService

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

def handle_migrate(db: Database):
    db.apply_migrations(config.migrations_dir)
    print("Schema migrations applied successfully.")

def handle_seed(db: Database):
    db.apply_migrations(config.migrations_dir)
    print("Database seeded successfully.")

def handle_report(service: AnalyticsService, report_type: str, threshold: float):
    if report_type == "daily":
        results = service.get_daily_cost_per_user()
        for r in results:
            print(f"{r['user_id']} | {r['usage_date']} | ${r['total_cost']:.4f} | {r['total_tokens']} tokens")
    elif report_type == "models":
        results = service.get_model_utilization()
        for r in results:
            print(f"{r['model_name']} | {r['request_count']} reqs | {r['total_tokens']} tokens | ${r['total_cost']:.4f}")
    elif report_type == "spikes":
        results = service.get_cost_spikes(threshold=threshold)
        for r in results:
            print(f"SPIKE: {r['user_id']} | {r['usage_date']} | ${r['daily_spend']:.4f}")
    elif report_type == "trends":
        results = service.get_token_trends()
        for r in results:
            print(f"{r['usage_date']} | {r['model_name']} | tokens={r['total_tokens']} | est=${r['estimated_cost']}")

def handle_export(service: AnalyticsService, output_path: str):
    results = service.get_daily_cost_per_user()
    if results:
        with open(output_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=list(results[0].keys()))
            writer.writeheader()
            writer.writerows(results)
    print(f"Exported {len(results)} records to {output_path}")

def main(args=None):
    parser = create_parser()
    opts = parser.parse_args(args)
    if not opts.command:
        parser.print_help()
        return 0

    db = Database(config.db_path)
    service = AnalyticsService(db)

    if opts.command == "migrate":
        handle_migrate(db)
    elif opts.command == "seed":
        handle_seed(db)
    elif opts.command == "report":
        handle_report(service, opts.type, opts.threshold)
    elif opts.command == "export":
        handle_export(service, opts.output)
    return 0
