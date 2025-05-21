import nltk
from nltk.corpus import stopwords


def removeStopWords(sentence: str) -> str: 
    nltk.download('stopwords') 

    stop_words = set(stopwords.words('portuguese')) 

    words = sentence.split() 

    filtered_words = [word for word in words if word not in stop_words] 
    
    return ' '.join(filtered_words)