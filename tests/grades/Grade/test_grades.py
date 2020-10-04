"""Tests grades.

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

from src.grades import Grade

# ==== CONSTANTS DEFINITIONS ==================================================


# ==== TEST LAUNCH ============================================================
class TestGradeGrades(unittest.TestCase):
    """Test for method grades.

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
        self._grade = Grade("./src/grades/french.alt.json")

    @timeout_decorator.timeout(30)
    def test_1(self) -> None:
        """Test 1."""
        grades = self._grade.grades
        assert "name" not in grades
