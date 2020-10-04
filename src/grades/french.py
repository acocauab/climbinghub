"""FILE TITLE.

Short description
"""

# ==== IMPORTS SECTION ========================================================
import json
# ==== CONSTANTS DEFINITIONS ==================================================

# ==== CLASS DEFINITION =======================================================
big = range(4, 10)
letters = ["a", "b", "c"]
extra = ["", "+"]

grades = {
    "1": 100,
    "2": 200,
    "3": 300
}

for num in big:
    for letter in letters:
        for plus in extra:
            if num <= 5 and plus == "+":
                continue
            original = str(num)+letter+plus
            extra_value = 0 if plus == "" else 5
            internal = num*100 + (letters.index(letter)+1)*10 + extra_value
            grades[original] = internal

with open("french.json", "w") as fp:
    json.dump(grades, fp, indent=4)
