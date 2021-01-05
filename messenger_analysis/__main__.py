'''
messenger_analysis is a tool to help you discover fun and interesting stats about
your messenging habits.
'''


from .cli.arguments import parse_arguments
from .cli.config import CONFIG
from .chat.parse import parse_chats
from .chat.filter import filter_chats


def main(args=None):
    '''Main entry point'''
    parse_arguments(args)
    chats = parse_chats(CONFIG.datasource)
    chats = filter_chats(chats)


if __name__ == '__main__':
    main()
