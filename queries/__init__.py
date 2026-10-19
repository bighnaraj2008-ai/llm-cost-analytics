"""Analytical SQL queries module for LLM Cost Analytics."""
import os

QUERIES_DIR = os.path.dirname(os.path.abspath(__file__))

def get_query(name: str) -> str:
    """Load query text by filename."""
    if not name.endswith('.sql'):
        name = f"{name}.sql"
    filepath = os.path.join(QUERIES_DIR, name)
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Query file '{name}' not found at {filepath}")
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()
