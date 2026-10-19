SELECT
    p.model_name,
    COUNT(r.id) as request_count,
    SUM(r.total_tokens) as total_tokens,
    SUM((r.prompt_tokens / 1000.0 * p.input_cost_per_1k_tokens) +
        (r.completion_tokens / 1000.0 * p.output_cost_per_1k_tokens)) as total_cost,
    AVG(r.latency_ms) as avg_latency_ms
FROM api_requests r
JOIN model_pricing p ON r.model_id = p.id
GROUP BY p.model_name
ORDER BY total_cost DESC;
