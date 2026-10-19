import unittest
from src.exceptions import (
    AnalyticsError,
    DatabaseConnectionError,
    MigrationError,
    QueryExecutionError,
    PricingTierNotFoundError,
    InputValidationError
)

class TestExceptions(unittest.TestCase):
    def test_inheritance_hierarchy(self):
        self.assertTrue(issubclass(DatabaseConnectionError, AnalyticsError))
        self.assertTrue(issubclass(MigrationError, AnalyticsError))
        self.assertTrue(issubclass(QueryExecutionError, AnalyticsError))
        self.assertTrue(issubclass(PricingTierNotFoundError, AnalyticsError))
        self.assertTrue(issubclass(InputValidationError, AnalyticsError))

    def test_exception_messages(self):
        err = PricingTierNotFoundError("Model 'test-model' not found")
        self.assertEqual(str(err), "Model 'test-model' not found")

if __name__ == "__main__":
    unittest.main()
