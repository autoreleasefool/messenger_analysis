'''String tokenization'''


import string
from typing import Dict, List
from sklearn.feature_extraction.text import CountVectorizer, ENGLISH_STOP_WORDS
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


STEMMER = PorterStemmer()


def strip_punctuation(messages: List[str]) -> List[str]:
    '''Strip all punctuation from messages'''
    return [''.join([ch for ch in x if ch not in string.punctuation]) for x in messages]


def stem_messages(messages: List[str]) -> List[List[str]]:
    '''Returns stemmed words for contents of each message'''
    return [[STEMMER.stem(y) for y in x.split()] for x in messages]
