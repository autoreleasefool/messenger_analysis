'''CLI argument parsing'''


from argparse import ArgumentParser
from typing import Any, List
import sys


def parse_arguments(args: List[Any] = None):
    '''Parses CLI arguments'''
    if args is None:
        args = sys.argv[1:]

    parser = ArgumentParser(description='explore your messaging habits')

    # Input
    parser.add_argument('-d', '--datasource',
                        action='store_true',
                        help='messenger data directory. defaults to ./data')

    # Output

    # Filtering
    parser.add_argument('--filterNames',
                        nargs=1,
                        help='comma-separated list of names to include')
    parser.add_argument('--excludeGroups',
                        action='store_true',
                        help='exclude group chats with >2 participants')

    return parser.parse_args(args)
