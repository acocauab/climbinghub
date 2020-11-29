"""Tests analyze.

Links of intetest:
Mocks
https://docs.python.org/3/library/unittest.mock-examples.html#partial-mocking
Asserts
https://docs.python.org/3/library/unittest.html#deprecated-aliases
Timeouts
https://github.com/pnpnpn/timeout-decorator
"""
# ==== IMPORTS SECTION ========================================================
import unittest
from unittest.mock import patch
import timeout_decorator

from src.analyzer import Analyzer

# ==== CONSTANTS DEFINITIONS ==================================================


# ==== TEST LAUNCH ============================================================
class TestAnalyzerAnalyze(unittest.TestCase):
    """Test for method analyze.

    Special functions:
        setUpClass -> Executed once bafore all test cases.
        setUp -> Executed once before each test function.
        test* -> Where the test should be.
        tearDown -> Executed once after each test function.
        tearDownClass -> Executed once after all test cases
    """

    @timeout_decorator.timeout(30)
    def setUp(self) -> None:
        """Set up variables for testing."""
        self._analyzer = Analyzer("", "<title>Hola 6a+</title>")

    @timeout_decorator.timeout(30)
    def test_1(self) -> None:
        """Test 1."""
        self._analyzer.analyze()
        print(self._analyzer.route)
        self._analyzer.route["name"] = "Hola 6a+"
        self._analyzer.route["grade"]["climbing"] = 615
