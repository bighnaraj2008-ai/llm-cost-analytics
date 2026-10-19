import os
from dataclasses import dataclass

@dataclass
class Config:
    """Application configuration handler."""
    base_dir: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    db_path: str = os.path.join(base_dir, "analytics.db")
    migrations_dir: str = os.path.join(base_dir, "migrations")
    queries_dir: str = os.path.join(base_dir, "queries")
    default_spike_threshold: float = 10.0
    env: str = os.getenv("APP_ENV", "development")

config = Config()
