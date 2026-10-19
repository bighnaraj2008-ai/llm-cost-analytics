import unittest
import logging
from src.logger import get_logger

class TestLogger(unittest.TestCase):
    def test_get_logger_instance(self):
        logger = get_logger("test-logger", logging.DEBUG)
        self.assertIsNotNone(logger)
        self.assertEqual(logger.name, "test-logger")
        self.assertEqual(logger.level, logging.DEBUG)

if __name__ == "__main__":
    unittest.main()
