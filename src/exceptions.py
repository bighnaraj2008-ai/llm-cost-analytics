"""Custom analytics exception classes."""

class AnalyticsError(Exception):
    """Base exception for LLM Cost Analytics."""
    pass

class DatabaseConnectionError(AnalyticsError):
    """Raised when connecting to SQLite fails."""
    pass

class MigrationError(AnalyticsError):
    """Raised when database schema migration execution fails."""
    pass

class QueryExecutionError(AnalyticsError):
    """Raised when an analytical query fails."""
    pass

class PricingTierNotFoundError(AnalyticsError):
    """Raised when a model pricing tier is not registered."""
    pass

class InputValidationError(AnalyticsError):
    """Raised when telemetry input validation fails."""
    pass
