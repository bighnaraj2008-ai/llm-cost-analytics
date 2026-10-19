# Internal Python Module API Reference

## `src.database.Database`
SQLite database wrapper providing transaction handling, WAL configuration, and schema migration execution.

- `__init__(db_path: str = ":memory:", timeout: float = 30.0)`
- `connect() -> sqlite3.Connection`
- `execute(sql: str, params: tuple = ()) -> sqlite3.Cursor`
- `apply_migrations(migrations_dir: str) -> None`

## `src.services.cost_calculator.CostCalculator`
Pure mathematical engine for token cost computation.

- `calculate_cost(prompt_tokens: int, completion_tokens: int, input_cost_per_1k: float, output_cost_per_1k: float) -> float`
- `calculate_for_model(model_name: str, prompt_tokens: int, completion_tokens: int, pricing_tiers: dict, multiplier: float = 1.0) -> float`

## `src.services.analytics.AnalyticsService`
Orchestrator for SQL analytical aggregation queries.

- `get_daily_cost_per_user() -> List[dict]`
- `get_model_utilization() -> List[dict]`
- `get_cost_spikes(threshold: float = 10.0) -> List[dict]`
- `get_token_trends() -> List[dict]`
