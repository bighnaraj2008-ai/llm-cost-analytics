# Analytical SQL Workloads Documentation

This document describes the analytical SQL queries provided in `queries/`.

## 1. Daily Cost Per User (`daily_cost_per_user.sql`)
- **Purpose**: Computes the daily token consumption and aggregated dollar spend per user.
- **Complexity**: O(N) aggregate scan utilizing `idx_api_requests_user_id` and `idx_api_requests_created_at`.
- **Output Columns**: `user_id`, `usage_date`, `total_cost`, `total_tokens`, `request_count`.

## 2. Model Utilization Breakdown (`model_utilization_breakdown.sql`)
- **Purpose**: Compares total request volume, token throughput, spend, and average latency across models.
- **Complexity**: Grouped aggregation utilizing `idx_api_requests_model_id`.

## 3. Cost Spike Detector (`cost_spike_detector.sql`)
- **Purpose**: Flags users whose daily spend exceeds a configured threshold (default: $10.00).
- **Technique**: Common Table Expression (CTE) computing user daily spend filtered by threshold clause.

## 4. Token Trend Analysis (`token_trend_analysis.sql`)
- **Purpose**: Evaluates rolling consumption trends across models over time.
