"""Demonstrates programmatic insertion of custom self-hosted model pricing tiers."""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.database import Database
from src.config import config
from src.models.pricing import PricingTier

def main():
    db = Database(":memory:")
    db.apply_migrations(config.migrations_dir)

    # Register custom self-hosted Llama-3-70B model tier
    custom_tier = PricingTier(
        model_name="llama-3-70b-instruct",
        input_cost_per_1k_tokens=0.0008,
        output_cost_per_1k_tokens=0.0012,
        tier_type="self-hosted"
    )

    db.execute(
        """INSERT INTO model_pricing (model_name, input_cost_per_1k_tokens, output_cost_per_1k_tokens, tier_type)
           VALUES (?, ?, ?, ?);""",
        (custom_tier.model_name, custom_tier.input_cost_per_1k_tokens, custom_tier.output_cost_per_1k_tokens, custom_tier.tier_type)
    )
    db.commit()

    cursor = db.execute("SELECT * FROM model_pricing WHERE model_name = ?", (custom_tier.model_name,))
    row = dict(cursor.fetchone())
    print("Registered Custom Model Tier:", row)

if __name__ == "__main__":
    main()
