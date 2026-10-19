# LLM Cost Analytics Engine

[![CI](https://github.com/bighnaraj2008-ai/llm-cost-analytics/actions/workflows/ci.yml/badge.svg)](https://github.com/bighnaraj2008-ai/llm-cost-analytics/actions)
[![Python 3.11 | 3.12](https://img.shields.io/badge/python-3.11%20%7C%203.12-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code Style: Flake8](https://img.shields.io/badge/code%20style-flake8-000000.svg)](https://flake8.pycqa.org/)

A production-grade relational database schema and analytical SQL aggregation engine designed to track token consumption, calculate tiered model costs, run daily user spend breakdowns, analyze model utilization, and detect cost spikes using SQL analytical queries and SQLite.

## Core Features
- **Accurate Token Pricing**: Separate accounting for prompt and completion token costs.
- **Referential Integrity**: Strict foreign key constraints and cascade rules.
- **High-Performance Analytics**: Indexed SQL aggregations for daily spend, model usage, and spikes.
- **Extensible CLI**: Subcommands for database migrations, seeding, report viewing, and CSV exports.

## Documentation Index
- [System Architecture & Schema Design](docs/ARCHITECTURE.md)
- [Analytical SQL Workloads](docs/ANALYTICAL_QUERIES.md)
- [Internal API Reference](docs/API.md)
- [LLM Cost Optimization Guide](docs/COST_OPTIMIZATION_GUIDE.md)
- [Performance Benchmark Results](docs/BENCHMARK_RESULTS.md)
- [Frequently Asked Questions (FAQ)](docs/FAQ.md)
- [Troubleshooting Guide](docs/TROUBLESHOOTING.md)

## Installation & Quickstart

```bash
# Clone the repository
git clone https://github.com/bighnaraj2008-ai/llm-cost-analytics.git
cd llm-cost-analytics

# Install dependencies
pip install -r requirements.txt

# Run full test suite
pytest
```

## CLI Usage

```bash
# Run schema migrations
python -m src.main migrate

# Seed default pricing tiers and sample telemetry
python -m src.main seed

# View daily user cost breakdown
python -m src.main report --type daily

# View model utilization breakdown
python -m src.main report --type models

# Detect anomalous cost spikes (> $10.00 spend)
python -m src.main report --type spikes --threshold 10.0

# Export daily costs to CSV
python -m src.main export --output daily_costs.csv
```

## License
Distributed under the MIT License. See [LICENSE](LICENSE) for more information.
