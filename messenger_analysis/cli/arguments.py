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
                        default=os.path.join('.', 'data'),
                        help='messenger data directory. defaults to ./data')

    # Output

    # Filtering
    parser.add_argument('--includeNames',
                        nargs=1,
                        help='comma-separated list of names to include')
    parser.add_argument('--excludeGroups',
                        action='store_true',
                        help='exclude group chats with >2 participants')
    parser.add_argument('--excludeArchived',
                        action='store_true',
                        help='exclude archived chats')

    # Debug
    parser.add_argument('--validate',
                        action='store_true',
                        help='debug. perform additional validation on dataset')

    CONFIG.update(parser.parse_args(args))
