'''Search functions'''


import os


def search_files(directory='.', extension=''):
    '''Search for files with a given extension in a certain directory, recursively'''
    all_files = []
    extension = extension.lower()
    for dirpath, _, files in os.walk(directory):
        for name in files:
            if extension and name.lower().endswith(extension):
                all_files.append(os.path.join(dirpath, name))
            elif not extension:
                all_files.append(os.path.join(dirpath, name))
    return all_files
