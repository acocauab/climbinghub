"""Tests get_all_links.

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
import asyncio

from src.retriever import Retriever

# ==== CONSTANTS DEFINITIONS ==================================================


# ==== TEST LAUNCH ============================================================
class TestRetrieverGetAllLinks(unittest.TestCase):
    """Test for method get_all_links.

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
        async def mock(x, y):
            return None
        self._retriever.db.store_url = mock
        self.loop = asyncio.get_event_loop()

    @timeout_decorator.timeout(30)
    def test_1(self) -> None:
        """Test 1."""
        self.loop.run_until_complete(
            self._retriever.get_all_links(
                '<a href="https://www.google.es/gmail">google</a>')
        )

        assert self._retriever.visited[0] == "https://www.google.es/gmail"
