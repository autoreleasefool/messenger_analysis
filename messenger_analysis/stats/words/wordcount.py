'''Analyze counts of words in chats'''


import matplotlib.pyplot as plt
from typing import Dict, List, Tuple
from sklearn.feature_extraction.text import CountVectorizer
from messenger_analysis.chat.chat import Chat
from messenger_analysis.cli.config import CONFIG
from messenger_analysis.util.lists import flatten
from messenger_analysis.util.stopwords import get_stop_words
from messenger_analysis.util.tokenize import strip_punctuation, should_include_word


def count_words(chats: List[Chat]) -> Dict[str, int]:
    '''Returns number of occurrences of each word in the chat'''
    # tokenized = tokenize_chats(chats)
    messages = flatten([x.messages for x in chats])
    messages = [x.content for x in messages if x.content]
    messages = strip_punctuation(messages)

    vec = CountVectorizer(stop_words=get_stop_words()).fit(messages)
    bag_of_words = vec.transform(messages)
    sum_words = bag_of_words.sum(axis=0)
    words_freq = {word: sum_words[0, idx] for word, idx in vec.vocabulary_.items() if should_include_word(word)}
    return words_freq


def top_n_words(chats: List[Chat], count: int) -> List[Tuple[str, int]]:
    '''Returns the top 10 words uttered in the chat'''
    wordcounts = count_words(chats)
    word_freq = [(word, wordcounts[word]) for word in wordcounts]
    word_freq = sorted(word_freq, key=lambda x: x[1], reverse=True)
    return word_freq[:min(count, len(word_freq))]


def plot_top_n_words(chats: List[Chat]):
    top_words = top_n_words(chats, CONFIG.plotTopWords)
    _produce_figure(top_words)


def _produce_figure(frequencies: List[Tuple[str, int]]):
    words = [x[0] for x in reversed(frequencies)]
    counts = [x[1] for x in reversed(frequencies)]

    plt.clf()
    plt.title(f'Usage of top {len(frequencies)} words')

    fig, ax = plt.subplots(figsize=(10, len(frequencies) // 5))
    ax.barh(words, counts)
    plt.ylabel('Words')
    plt.xlabel('Total usages')

    for i, v in enumerate(counts):
        ax.text(v + 3, i - 0.25, str(v))

    plt.tight_layout()
    plt.savefig(CONFIG.get_output_filename(f'top_{len(frequencies)}_words.png'))
