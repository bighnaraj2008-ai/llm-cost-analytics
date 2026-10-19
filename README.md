# LLM Cost Analytics Engine

A production-grade relational database schema and analytical SQL aggregation engine designed to track token consumption, calculate tiered model costs, run daily user spend breakdowns, analyze model utilization, and detect cost spikes using SQL analytical queries and SQLite.

## Core Features
- **Accurate Token Pricing**: Separate accounting for prompt and completion token costs.
- **Referential Integrity**: Strict foreign key constraints and cascade rules.
- **High-Performance Analytics**: Indexed SQL aggregations for daily spend, model usage, and spikes.
- **Extensible CLI**: Subcommands for database migrations, seeding, report viewing, and CSV exports.

## Cost Optimization
For enterprise architectures and best practices on reducing inference spend, see our [Cost Optimization Guide](docs/COST_OPTIMIZATION_GUIDE.md).

## Installation & Setup

1. **Clone repository**:
   ```bash
   git clone https://github.com/bighnaraj2008-ai/llm-cost-analytics.git
   cd llm-cost-analytics
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run tests**:
   ```bash
   pytest
   ```

## CLI Usage Guide

```bash
# Run schema migrations
python -m src.main migrate

# Seed sample pricing and telemetry
python -m src.main seed

# View daily user cost breakdown
python -m src.main report --type daily
```
