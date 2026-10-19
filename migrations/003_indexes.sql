-- Migration 003: Performance indexes
CREATE INDEX IF NOT EXISTS idx_api_requests_user_id ON api_requests(user_id);
CREATE INDEX IF NOT EXISTS idx_api_requests_model_id ON api_requests(model_id);
CREATE INDEX IF NOT EXISTS idx_api_requests_created_at ON api_requests(created_at);
CREATE INDEX IF NOT EXISTS idx_model_pricing_name ON model_pricing(model_name);
