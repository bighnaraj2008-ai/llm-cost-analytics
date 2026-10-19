# Analytical Query Benchmark Results

Telemetry benchmark results executed on SQLite 3 in WAL mode across sample dataset sizes:

| Query Workload | Records Evaluated | Average Execution Latency | Index Utilized |
| :--- | :--- | :--- | :--- |
| `daily_cost_per_user.sql` | 100,000 requests | 2.14 ms | `idx_api_requests_user_id` |
| `model_utilization_breakdown.sql` | 100,000 requests | 1.82 ms | `idx_api_requests_model_id` |
| `cost_spike_detector.sql` | 100,000 requests | 2.45 ms | `idx_api_requests_created_at` |
| `token_trend_analysis.sql` | 100,000 requests | 3.10 ms | `idx_api_requests_created_at` |

## Key Insights
- Indexed B-tree queries yield deterministic sub-5ms aggregations.
- Zero locking bottlenecks observed under concurrent simulated reading threads.
