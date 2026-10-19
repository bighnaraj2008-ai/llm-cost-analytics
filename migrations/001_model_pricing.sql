-- Migration 001: Model pricing table for token tier billing
CREATE TABLE IF NOT EXISTS model_pricing (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    model_name TEXT UNIQUE NOT NULL,
    input_cost_per_1k_tokens REAL NOT NULL,
    output_cost_per_1k_tokens REAL NOT NULL,
    tier_type TEXT DEFAULT 'standard',
    effective_date DATETIME DEFAULT CURRENT_TIMESTAMP
);
