"""FILE TITLE.

Short description
"""

# ==== IMPORTS SECTION ========================================================
import json
# ==== CONSTANTS DEFINITIONS ==================================================

# ==== CLASS DEFINITION =======================================================
grades = {}
for i in range(0, 10):
    grades["A"+str(i)] = i*10

with open("artificial.json", "w") as fp:
    json.dump(grades, fp, indent=4)
