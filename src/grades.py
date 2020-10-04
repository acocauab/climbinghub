"""Class to represent grades from json.

On instance of this class will be instanced for each definition of grade we
have in the json formats.
"""

# ==== IMPORTS SECTION ========================================================
import json
# ==== CONSTANTS DEFINITIONS ==================================================


# ==== CLASS DEFINITION =======================================================
class Grade():
    """Grade class definition."""

    def __init__(self, definition: str) -> None:
        """__init__.

        Args:
            definition (str): Json definition of the grade
        """
        with open(definition) as fp:
            self._grades = json.load(fp)

    @property
    def grades(self) -> list:
        """Get list of grade names.

        Args:

        Returns:
            list: of string grades
        """
        grades = list(self._grades.keys())
        grades.remove("name")
        return grades

    @property
    def name(self) -> str:
        """Get the grade name.

        Returns:
            str: Grade name
        """
        return self._grades["name"]

    def grade_to_int(self, grade: str) -> int:
        """Convert grade to internal integer representation.

        Args:
            grade (str): origninal string grade

        Returns:
            int: internal representation
        """
        return self._grades[grade]
