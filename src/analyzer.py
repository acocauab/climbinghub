"""FILE TITLE.

Short description
"""

# ==== IMPORTS SECTION ========================================================
import os
from urllib.parse import urlparse
import pathlib
from bs4 import BeautifulSoup
from . import grades
import logging
import nltk
# ==== CONSTANTS DEFINITIONS ==================================================
GRADES_DIR = str(pathlib.Path(__file__).parent.absolute()) + "/grades"
logger = logging.getLogger(__name__)


# ==== CLASS DEFINITION =======================================================
class Analyzer():
    """Analyze the webpage looking for climbing routes."""

    def __init__(self, website: str, webpage: str) -> None:
        """Iniialize.

        Create default values for route and parse the webpage to be able
        to extract content in the future.

        Args:
            website (str): website
            webpage (str): webpage

        """
        self.original_webpage = webpage
        self.webpage = BeautifulSoup(webpage, 'html.parser')
        self.route = {}
        self.route["_id"] = webpage
        self.route["website"] = website
        self.route["grade"] = {}  # type:ignore
        self.route["photos"] = []  # type:ignore
        self.website = website
        self.grades = {}

        # Initialize grades
        for path in os.listdir(GRADES_DIR):

            if os.path.isdir(path):
                continue
            if ".json" not in path:
                continue

            print(GRADES_DIR + "/" + path)
            g = grades.Grade(GRADES_DIR + "/" + path)
            # TODO: Check for duplicate grades.
            self.grades[g.name] = g

    def _parse_grades(self) -> None:
        # Initialize grade
        for grade in self.grades.values():
            self.route["grade"][grade.id] = None

        def get_grades(text: str) -> None:
            words_fdist = self.process_text(text)
            print(words_fdist)
            # NOTE: Do we miss here a sort of words_fdist?
            for grade in self.grades.values():
                if grade.check_grade(words_fdist) is None:
                    continue
                f_grade = grade.grade_to_int(
                    grade.check_grade(words_fdist))
                if f_grade is not None and not self.route["grade"][grade.id]:
                    self.route["grade"][grade.id] = final_grade

        title = self.webpage.find('title')
        get_grades(title.text)

        # headers = [
        #     tag.text for tag in self.webpage.find_all(["h1", "h2", "h3"])]
        # headers = " ".join(headers)
        # get_grades(headers)
        # soup = BeautifulSoup(self.original_webpage, 'html.parser')
        # soup.extract(a)

    def _parse_tags(self) -> None:
        pass

    def _parse_name(self) -> None:
        logger.info("Parsing image name")
        self.route["name"] = self.webpage.title.string

    def _parse_photos(self) -> None:
        logger.info("Parsing web images")
        for img in self.webpage.findAll('img'):
            img = img["src"]
            hostname = urlparse(img).netloc
            if hostname == self.website:
                self.route["photos"].append(img)  # type: ignore

    def _parse_gps(self) -> None:
        # TODO: To be done in the future.
        pass

    def process_text(self, text):
        words = nltk.word_tokenize(text)
        # TODO: Remove stop words
        fdist = nltk.probability.FreqDist(words)
        return fdist.most_common()
