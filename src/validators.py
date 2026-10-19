from typing import Dict, Any

class ValidationError(ValueError):
    """Raised when data validation fails."""
    pass

def validate_token_count(tokens: int) -> int:
    """Validate token count is non-negative integer."""
    if not isinstance(tokens, int) or tokens < 0:
        raise ValidationError(f"Token count must be a non-negative integer, got {tokens}")
    return tokens

def validate_cost_rate(rate: float) -> float:
    """Validate rate is non-negative float."""
    if not isinstance(rate, (int, float)) or rate < 0:
        raise ValidationError(f"Cost rate must be a non-negative number, got {rate}")
    return float(rate)

def validate_user_id(user_id: str) -> str:
    """Validate user ID is non-empty string."""
    if not user_id or not str(user_id).strip():
        raise ValidationError("User ID cannot be empty or whitespace")
    return str(user_id).strip()

def validate_pricing_tier(tier_data: Dict[str, Any]) -> Dict[str, Any]:
    """Validate pricing tier dictionary schema."""
    required = ["model_name", "input_cost_per_1k_tokens", "output_cost_per_1k_tokens"]
    for field in required:
        if field not in tier_data:
            raise ValidationError(f"Missing required pricing tier field: '{field}'")
    validate_cost_rate(tier_data["input_cost_per_1k_tokens"])
    validate_cost_rate(tier_data["output_cost_per_1k_tokens"])
    return tier_data
