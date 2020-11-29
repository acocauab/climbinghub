"""FILE TITLE.

Short description
"""

# ==== IMPORTS SECTION ========================================================

# ==== CONSTANTS DEFINITIONS ==================================================

# ==== CLASS DEFINITION =======================================================
import logging
from colorlog import ColoredFormatter
LOG_LEVEL = logging.DEBUG
LOGFORMAT =\
    "%(log_color)s%(levelname)-8s%(reset)s | %(log_color)s%(message)s%(reset)s"
logging.root.setLevel(LOG_LEVEL)
formatter = ColoredFormatter(LOGFORMAT)
stream = logging.StreamHandler()
stream.setLevel(LOG_LEVEL)
stream.setFormatter(formatter)
logger = logging.getLogger('climbing_hub')
logger.setLevel(LOG_LEVEL)
logger.addHandler(stream)
