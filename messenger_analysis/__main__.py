'''
messenger_analysis is a tool to help you discover fun and interesting stats about
your messenging habits.
'''


import json
import os
from .cli.arguments import parse_arguments


def import_data(datasource=None):
    '''Import messenger data'''
    if datasource is None:
        datasource = os.path.join('.', 'data')
    with open(datasource, 'r') as data:
        return json.load(data.read())
    return None


def main(args=None):
    '''Main entry point'''
    args = parse_arguments(args)
    data = import_data(args)


if __name__ == '__main__':
    main()
