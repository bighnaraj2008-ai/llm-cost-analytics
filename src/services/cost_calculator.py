class CostCalculator:
    """Core mathematical engine for calculating token costs."""

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
