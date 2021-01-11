'''String tokenization'''


import re
import string
from typing import Dict, List
from sklearn.feature_extraction.text import CountVectorizer, ENGLISH_STOP_WORDS
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from messenger_analysis.cli.config import CONFIG


STEMMER = PorterStemmer()


def strip_punctuation(messages: List[str]) -> List[str]:
    '''Strip all punctuation from messages'''
    return [''.join([ch for ch in x if ch not in string.punctuation and ch != "\u00e2"]) for x in messages]


def stem_messages(messages: List[str]) -> List[List[str]]:
    '''Returns stemmed words for contents of each message'''
    return [[STEMMER.stem(y) for y in x.split()] for x in messages]


def should_include_word(word: str) -> bool:
    if word in CONFIG.exclude_words:
        return False
    if CONFIG.include_words and word not in CONFIG.include_words:
        return False
    if CONFIG.match_exclude_words and re.search(CONFIG.match_exclude_words, word):
        return False
    if CONFIG.match_words and not re.search(CONFIG.match_words, word):
        return False
    return True
