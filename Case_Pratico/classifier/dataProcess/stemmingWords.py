from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from functools import reduce
import nltk

def stemmingWords(msg: str):
    nltk.download('punkt_tab')

    ps = PorterStemmer()

    words = word_tokenize(msg)

    stemmed_sentence = reduce(lambda x, y: x + " " + ps.stem(y), words, "")

    return stemmed_sentence