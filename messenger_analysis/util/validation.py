'''Data validation'''


from typing import Set
from messenger_analysis.cli.config import CONFIG


def validate_keys(module_name: str, keys: Set[str], valid_keys: Set[str]):
    '''Validate keys compared to a set of valid keys'''
    if not CONFIG.validate:
        return
    if not keys.issubset(valid_keys):
        print(f'invalid {module_name} keys:', keys - valid_keys)
