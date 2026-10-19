SELECT
    date(r.created_at) as usage_date,
    p.model_name,
    SUM(r.prompt_tokens) as total_prompt_tokens,
    SUM(r.completion_tokens) as total_completion_tokens,
    SUM(r.total_tokens) as total_tokens,
    ROUND(SUM((r.prompt_tokens / 1000.0 * p.input_cost_per_1k_tokens) +
              (r.completion_tokens / 1000.0 * p.output_cost_per_1k_tokens)), 4) as estimated_cost
FROM api_requests r
JOIN model_pricing p ON r.model_id = p.id
GROUP BY usage_date, p.model_name
ORDER BY usage_date ASC, total_tokens DESC;
