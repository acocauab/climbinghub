"""Tests check_grade.

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
from src import grades

# ==== CONSTANTS DEFINITIONS ==================================================


# ==== TEST LAUNCH ============================================================
class TestGradeCheckGrade(unittest.TestCase):
    """Test for method check_grade.

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
        r = self._grade.check_grade(["nothing", "here"])
        self.assertEqual(r, grades.NO_GRADE)

    @timeout_decorator.timeout(30)
    def test_2(self) -> None:
        """Test 2."""
        r = self._grade.check_grade(["6b", "here"])
        self.assertEqual(r, "6b")
