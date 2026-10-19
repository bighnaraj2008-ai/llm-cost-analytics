-- Migration 004: Seed default LLM pricing tiers
INSERT OR IGNORE INTO model_pricing (model_name, input_cost_per_1k_tokens, output_cost_per_1k_tokens, tier_type) VALUES
('gpt-4', 0.03, 0.06, 'premium'),
('gpt-3.5-turbo', 0.0015, 0.002, 'standard'),
('claude-3-opus', 0.015, 0.075, 'premium'),
('claude-3-sonnet', 0.003, 0.015, 'standard'),
('gemini-1.5-pro', 0.0035, 0.0105, 'standard'),
('gemini-1.5-flash', 0.00035, 0.00105, 'economy');
