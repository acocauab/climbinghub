"""Tests retrieve.

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
import asyncio
import timeout_decorator

from src.retriever import Retriever

# ==== CONSTANTS DEFINITIONS ==================================================


# ==== TEST LAUNCH ============================================================
class TestRetrieverRetrieve(unittest.TestCase):
    """Test for method retrieve.

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
        self._retriever = Retriever("https://www.google.es")
        self.loop = asyncio.get_event_loop()

    @timeout_decorator.timeout(30)
    def test_1(self) -> None:
        """Test 1."""
        self.loop.run_until_complete(self._retriever.retrieve())

    @timeout_decorator.timeout(30)
    def test_2(self) -> None:
        """Test 1."""
        self.loop.run_until_complete(
            self._retriever.retrieve("https://www.google.com"))
