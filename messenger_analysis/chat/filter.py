'''Chat filtering'''


from typing import List, Set
from messenger_analysis.cli.config import CONFIG
from .chat import Chat


def filter_chats(chats: List[Chat]) -> List[Chat]:
    '''Performs filtering based on app config'''
    if CONFIG.include_names:
        chats = _filter_by_participant(chats, CONFIG.include_names)
    if CONFIG.exclude_groups:
        chats = _filter_groups(chats)
    if CONFIG.exclude_archived:
        chats = _filter_archived(chats)
    return chats


def _filter_by_participant(chats: List[Chat], names: Set[str]) -> List[Chat]:
    '''Filters out chats that don't include any participants with the given names'''
    return filter(lambda x: not names.isdisjoint(x.participants), chats)


def _filter_groups(chats: List[Chat]) -> List[Chat]:
    '''Filters out chats that are groups'''
    return filter(lambda x: x.is_group, chats)


def _filter_archived(chats: List[Chat]) -> List[Chat]:
    '''Filters out chats that are archived'''
    return filter(lambda x: x.is_archived, chats)
