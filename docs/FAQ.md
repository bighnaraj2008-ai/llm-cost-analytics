# Frequently Asked Questions (FAQ)

## 1. Why SQLite instead of PostgreSQL for the initial analytics engine?
SQLite in WAL (Write-Ahead Logging) mode delivers exceptional single-node read throughput (tens of thousands of analytical reads per second) with zero deployment overhead, making it ideal for embedded pipelines, CLI analytics, and microservice telemetry.

## 2. How are partial thousand-token costs rounded?
Token costs are computed with 64-bit floating point precision (`prompt_tokens / 1000.0 * rate`) and rounded to 6 decimal places during calculation to prevent floating-point accumulation drift.

## 3. Can I dynamically adjust pricing for custom models?
Yes. Pricing tiers are defined in the `model_pricing` table and can be added or updated via SQL scripts or the `src.models.pricing` module.
