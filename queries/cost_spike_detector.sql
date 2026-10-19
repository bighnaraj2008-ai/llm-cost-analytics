-- Identifies users whose daily spend exceeds 10.0 units
WITH daily_costs AS (
    SELECT
        r.user_id,
        date(r.created_at) as usage_date,
        SUM((r.prompt_tokens / 1000.0 * p.input_cost_per_1k_tokens) +
            (r.completion_tokens / 1000.0 * p.output_cost_per_1k_tokens)) as daily_spend,
        SUM(r.total_tokens) as total_tokens,
        COUNT(r.id) as request_count
    FROM api_requests r
    JOIN model_pricing p ON r.model_id = p.id
    GROUP BY r.user_id, usage_date
)
SELECT
    user_id,
    usage_date,
    daily_spend,
    total_tokens,
    request_count
FROM daily_costs
WHERE daily_spend > 10.0
ORDER BY daily_spend DESC;
