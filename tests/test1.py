"""FILE TITLE.

Short description
"""

# ==== IMPORTS SECTION ========================================================

# ==== CONSTANTS DEFINITIONS ==================================================

# ==== CLASS DEFINITION =======================================================
from bs4 import BeautifulSoup
from bs4.element import Comment
import spacy
import nltk
import requests

# Parse website
# =============================================================================
def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]', "a", "img"]:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)
    return u" ".join(t.strip() for t in visible_texts)

# html = requests.get('https://www.rocjumper.com/escalada/via-nuria-serra-sant-joan-boxiols/').text
html = requests.get('https://www.klimbingspider.com/anglada-guillamon-cadireta/').text
text = text_from_html(html)


# Get words
# =============================================================================
sentences = nltk.sent_tokenize(text)
words = nltk.word_tokenize("Dificultad: V+/Ae Dificultad obligada: V+/A3e 6a 6a+")
# words = nltk.word_tokenize(text)
words_clean = []
stop_words = nltk.corpus.stopwords.words("spanish")
climbing_grades = ["I", "II", "III", "IV", "V", "6", "7", "8", "9"]
def word_contain_grades(word):
    for grade in climbing_grades:
        if grade in word:
            return True
    return False
for word in words:
    if not word.isalpha() and word_contain_grades(word):
        words_clean.append(word)
    # elif word_contain_grades(word):
    #     words_clean.append(word)

fdist = nltk.probability.FreqDist(words_clean)
print(fdist.most_common())
fdist.plot(50)
