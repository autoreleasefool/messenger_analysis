'''CLI argument parsing'''


import os
import sys
from argparse import ArgumentParser
from typing import Any, List
from .config import CONFIG


def parse_arguments(args: List[Any] = None):
    '''Parses CLI arguments'''
    if args is None:
        args = sys.argv[1:]

    parser = ArgumentParser(description='explore your messaging habits')

    # Input
    parser.add_argument('-d', '--datasource',
                        type=str,
                        default=os.path.join('.', 'data', 'messages'),
                        help='messenger data directory. defaults to ./data/messages')
    parser.add_argument('--stopwords',
                        type=str,
                        default=os.path.join('.', 'data', 'stopwords.txt'),
                        help='additional custom stopwords to ignore overrused words.' +
                             'each word should be on a separate line')

    # Output

    # Filtering chats
    parser.add_argument('--includeNames',
                        nargs=1,
                        help='comma-separated list of names to include')
    parser.add_argument('--excludeGroups',
                        action='store_true',
                        help='exclude group chats with >2 participants')
    parser.add_argument('--excludeArchived',
                        action='store_true',
                        help='exclude archived chats')

    # Filtering words
    parser.add_argument('--includeWords',
                        nargs=1,
                        help='comma-separated list of regexes for words to include')
    parser.add_argument('--excludeWords',
                        nargs=1,
                        help='comma-separated list of regexes for words to exclude')

    # Debug
    parser.add_argument('--validate',
                        action='store_true',
                        help='debug. perform additional validation on dataset')

    CONFIG.update(parser.parse_args(args))
