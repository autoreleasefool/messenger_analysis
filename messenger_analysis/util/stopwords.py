'''Stop words management'''


from typing import Set
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from nltk.corpus import stopwords
from messenger_analysis.cli.config import CONFIG


def get_stop_words() -> Set[str]:
    '''Get the list of stop words to use'''
    words = set(stopwords.words('english')).union(set(ENGLISH_STOP_WORDS))
    if CONFIG.stopwords:
        with open(CONFIG.stopwords, 'r') as data:
            words.update(data.read().split())
    return words
