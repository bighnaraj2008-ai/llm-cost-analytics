from dataclasses import dataclass
from typing import Optional

@dataclass
class APIRequestRecord:
    """API request usage record data model."""
    user_id: str
    model_id: int
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int
    id: Optional[int] = None
    status_code: int = 200
    latency_ms: float = 0.0
    created_at: Optional[str] = None
