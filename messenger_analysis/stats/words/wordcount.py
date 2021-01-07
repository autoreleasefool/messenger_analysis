'''Analyze counts of words in chats'''


from typing import Dict, List, Tuple
from sklearn.feature_extraction.text import CountVectorizer
from messenger_analysis.chat.chat import Chat
from messenger_analysis.util.lists import flatten
from messenger_analysis.util.stopwords import get_stop_words
from messenger_analysis.util.tokenize import strip_punctuation


def count_words(chats: List[Chat]) -> Dict[str, int]:
    '''Returns number of occurrences of each word in the chat'''
    # tokenized = tokenize_chats(chats)
    messages = flatten([x.messages for x in chats])
    messages = [x.content for x in messages if x.content]
    messages = strip_punctuation(messages)

    vec = CountVectorizer(stop_words=get_stop_words()).fit(messages)
    bag_of_words = vec.transform(messages)
    sum_words = bag_of_words.sum(axis=0)
    words_freq = {word: sum_words[0, idx] for word, idx in vec.vocabulary_.items()}
    return words_freq


def top_n_words(chats: List[Chat], count: int) -> List[Tuple[str, int]]:
    '''Returns the top 10 words uttered in the chat'''
    wordcounts = count_words(chats)
    word_freq = [(word, wordcounts[word]) for word in wordcounts]
    word_freq = sorted(word_freq, key=lambda x: x[1], reverse=True)
    return word_freq[:count]
