"""Tests _parse_tags.

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
class TestAnalyzerParseTags(unittest.TestCase):
    """Test for method _parse_tags.

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
        self._analyzer = Analyzer()

    @timeout_decorator.timeout(30)
    @unittest.skip("TODO")
    def test_1(self) -> None:
        """Test 1."""
        self._analyzer._parse_tags()

        self.assertEqual(Analyzer.__name__, "Analyzer")

        self.fail("TEST IS NOT IMPLEMENTED!")

    @timeout_decorator.timeout(30)
    @unittest.skip("TODO")
    def test_2(self) -> None:
        """Test 2."""
        with patch("src.analyzer.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.json = lambda: {"text": "Some Content"}

            self._analyzer._parse_tags()

        self.fail("TEST IS NOT IMPLEMENTED!")

    @timeout_decorator.timeout(30)
    @unittest.skip("TODO")
    def test_exception_1(self) -> None:
        """Test Expception 1."""
        self.assertRaises(Exception, self._analyzer._parse_tags)

        self.fail("TEST IS NOT IMPLEMENTED!")
