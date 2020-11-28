"""Class to represent grades from json.

On instance of this class will be instanced for each definition of grade we
have in the json formats.
"""

# ==== IMPORTS SECTION ========================================================
import json
# ==== CONSTANTS DEFINITIONS ==================================================
NO_GRADE = "NO_GRADE"


# ==== CLASS DEFINITION =======================================================
class Grade():
    """Grade class definition."""

    def __init__(self, definition: str) -> None:
        """__init__.

        Args:
            definition (str): Json definition of the grade
        """
        self.definition = definition
        with open(definition) as fp:
            self._grades = json.load(fp)

    @property
    def grades(self) -> list:
        """Get list of grade names.

        Args:

        Returns:
            list: of string grades
        """
        grades = list(self._grades["grades"].keys())
        return grades

    @property
    def name(self) -> str:
        """Get the grade name.

        Returns:
            str: Grade name
        """
        return self._grades["name"]

    @property
    def id(self) -> str:
        """Get grade id.

        Returns:
            str: Grade id
        """
        return self._grades["id"]

    def grade_to_int(self, grade: str) -> int:
        """Convert grade to internal integer representation.

        Args:
            grade (str): origninal string grade

        Returns:
            int: internal representation
        """
        return self._grades["grades"][grade]

    def check_grade(self, words: list) -> str:
        """Check if the grades are in a list of words.

        Args:
            words (list): List of words to check

        Returns:
            str: With the grade string
        """
        for word in words:
            if word in self.grades:
                return word
        return NO_GRADE
