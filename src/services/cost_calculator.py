from typing import Dict, Any

class CostCalculator:
    """Core mathematical engine for calculating token costs with tier matching and multiplier logic."""

    @staticmethod
    def calculate_cost(
        prompt_tokens: int,
        completion_tokens: int,
        input_cost_per_1k: float,
        output_cost_per_1k: float,
    ) -> float:
        input_cost = (prompt_tokens / 1000.0) * input_cost_per_1k
        output_cost = (completion_tokens / 1000.0) * output_cost_per_1k
        return round(input_cost + output_cost, 6)

    @classmethod
    def calculate_for_model(
        cls,
        model_name: str,
        prompt_tokens: int,
        completion_tokens: int,
        pricing_tiers: Dict[str, Dict[str, Any]],
        multiplier: float = 1.0,
    ) -> float:
        if model_name not in pricing_tiers:
            raise KeyError(f"Model '{model_name}' has no registered pricing tier")
        tier = pricing_tiers[model_name]
        input_rate = tier["input_cost_per_1k_tokens"] * multiplier
        output_rate = tier["output_cost_per_1k_tokens"] * multiplier
        return cls.calculate_cost(prompt_tokens, completion_tokens, input_rate, output_rate)
