from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from functools import reduce
import nltk

def stemmingWords():
    nltk.download('punkt_tab')

    ps = PorterStemmer()

    sentence = "Programmers program with programming languages"
    words = word_tokenize(sentence)

    # using reduce to apply stemmer to each word and join them back into a string
    stemmed_sentence = reduce(lambda x, y: x + " " + ps.stem(y), words, "")

    return stemmed_sentence