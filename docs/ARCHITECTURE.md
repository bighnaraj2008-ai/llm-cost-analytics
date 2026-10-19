# System Architecture & Design Documentation

## Overview
LLM Cost Analytics is an enterprise-grade analytics engine and relational schema tailored for tracking LLM token consumption, calculating tiered pricing models, detecting sudden cost spikes, and generating aggregated utilization telemetry.

## Entity-Relationship Architecture

```mermaid
erDiagram
    MODEL_PRICING ||--o{ API_REQUESTS : "categorizes"
    MODEL_PRICING {
        int id PK
        string model_name UK
        real input_cost_per_1k_tokens
        real output_cost_per_1k_tokens
        string tier_type
        datetime effective_date
    }
    API_REQUESTS {
        int id PK
        string user_id
        int model_id FK
        int prompt_tokens
        int completion_tokens
        int total_tokens
        int status_code
        real latency_ms
        datetime created_at
    }
```

## Schema Details
- **`model_pricing`**: Defines billing tiers per 1,000 prompt and completion tokens.
- **`api_requests`**: Stores request-level telemetry linked to model configurations with cascading referential integrity.
- **Indexes**: Composite and single-column indexes on `user_id`, `model_id`, and `created_at` ensure sub-millisecond query performance on large datasets.
