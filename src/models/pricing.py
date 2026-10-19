from dataclasses import dataclass
from typing import Optional

@dataclass
class PricingTier:
    """Pricing tier data model mapping."""
    model_name: str
    input_cost_per_1k_tokens: float
    output_cost_per_1k_tokens: float
    id: Optional[int] = None
    tier_type: str = "standard"
    effective_date: Optional[str] = None
