-- Migration 005: Sample mock request logs for testing aggregations
INSERT INTO api_requests (user_id, model_id, prompt_tokens, completion_tokens, total_tokens, status_code, latency_ms, created_at) VALUES
('user1', 1, 200000, 100000, 300000, 200, 1250.5, '2026-10-19 10:00:00'),
('user2', 2, 1000, 1000, 2000, 200, 210.2, '2026-10-19 11:00:00'),
('user3', 3, 50000, 25000, 75000, 200, 980.0, '2026-10-19 12:30:00'),
('user1', 2, 4000, 2000, 6000, 200, 320.1, '2026-10-18 15:45:00'),
('user2', 5, 10000, 5000, 15000, 200, 450.0, '2026-10-18 16:20:00'),
('user4', 6, 80000, 40000, 120000, 200, 180.4, '2026-10-19 09:15:00');
