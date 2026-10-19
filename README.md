# LLM Cost Analytics Engine

A production-grade relational database schema and analytical SQL aggregation engine designed to track token consumption, calculate tiered model costs, run daily user spend breakdowns, analyze model utilization, and detect cost spikes using SQL analytical queries and SQLite.

## Core Features
- **Accurate Token Pricing**: Separate accounting for prompt and completion token costs.
- **Referential Integrity**: Strict foreign key constraints and cascade rules.
- **High-Performance Analytics**: Indexed SQL aggregations for daily spend, model usage, and spikes.
- **Extensible CLI**: Subcommands for database migrations, seeding, report viewing, and CSV exports.

## Documentation
- [System Architecture](docs/ARCHITECTURE.md)
- [Analytical Queries](docs/ANALYTICAL_QUERIES.md)
- [API Reference](docs/API.md)
- [Cost Optimization Guide](docs/COST_OPTIMIZATION_GUIDE.md)
- [Frequently Asked Questions (FAQ)](docs/FAQ.md)

## Installation & Setup

```bash
git clone https://github.com/bighnaraj2008-ai/llm-cost-analytics.git
cd llm-cost-analytics
pip install -r requirements.txt
pytest
```
