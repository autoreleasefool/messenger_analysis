'''Wraps a datasource and provides details about the messages demarcated by that directory'''


import json
import operator
import os
import re
from typing import List, Set
from messenger_analysis.util.validation import validate_keys
from .message.message import Message
from .message.content import File, Photo, Video, SharedItem


class Chat:
    '''A list of messages'''
    _datasource: str
    name: str
    messages: List[Message] = []
    participants: Set[str] = set()
    is_archived: bool = False
    is_group: bool = False

    def __init__(self, datasource: str):
        self._datasource = datasource
        self.is_archived = 'archived_threads' in datasource
        message_files = [x for x in os.listdir(self._datasource) if re.match(r'message_\d+\.json$', x)]

        determined_properties = False

        for message_file in message_files:
            with open(os.path.join(datasource, message_file), 'r') as data:
                chat_json = json.load(data)
                self.participants.update([x['name'] for x in chat_json['participants']])
                self.messages.extend([Message(x) for x in chat_json['messages']])

                if not determined_properties:
                    determined_properties = True
                    self.name = chat_json['title']
                    self.is_group = chat_json['thread_type'] == 'RegularGroup'

        self.messages.sort(key=operator.attrgetter('timestamp'))

        validate_keys(
            'chat',
            set(chat_json.keys()),
            set(('participants', 'title', 'thread_type', 'messages', 'is_still_participant', 'thread_path'))
        )

    def get_files(self) -> List[File]:
        '''List of files shared in the chat'''
        return map(lambda x: x.files, self.messages)

    def get_photos(self) -> List[Photo]:
        '''List of photos shared in the chat'''
        return map(lambda x: x.photos, self.messages)

    def get_videos(self) -> List[Video]:
        '''List of videos shared in the chat'''
        return map(lambda x: x.videos, self.messages)

    def get_shares(self) -> List[SharedItem]:
        '''List of links shared in the chat'''
        return map(lambda x: x.shares, self.messages)
