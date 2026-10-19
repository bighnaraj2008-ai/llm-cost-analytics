"""System and threshold constants for LLM Cost Analytics."""

DEFAULT_SPIKE_THRESHOLD = 10.0
SUPPORTED_PROVIDERS = ("openai", "anthropic", "google")
SUPPORTED_MODELS = (
    "gpt-4",
    "gpt-3.5-turbo",
    "claude-3-opus",
    "claude-3-sonnet",
    "gemini-1.5-pro",
    "gemini-1.5-flash",
)
VERSION = "1.0.0"
