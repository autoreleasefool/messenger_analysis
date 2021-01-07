'''
messenger_analysis is a tool to help you discover fun and interesting stats about
your messenging habits.
'''


from .cli.arguments import parse_arguments
from .cli.config import CONFIG
from .chat.parse import parse_chats
from .chat.filter import filter_chats
from .stats.words.wordcount import top_n_words


def main(args=None):
    '''Main entry point'''
    parse_arguments(args)
    chats = parse_chats(CONFIG.datasource)
    chats = filter_chats(chats)
    print(top_n_words(chats, 100))


if __name__ == '__main__':
    main()
