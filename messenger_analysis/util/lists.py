'''Common list utilities'''


from typing import Any, List


def flatten(arg: List[List[Any]]) -> List[Any]:
    '''Flatten a 2D list to 1D'''
    return [item for sublist in arg for item in sublist]
