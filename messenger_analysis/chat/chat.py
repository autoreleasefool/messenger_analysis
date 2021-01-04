'''Wraps a datasource and provides details about the messages demarcated by that directory'''


import json
import operator
import os
import re
from typing import List, Set
from .message.message import Message
from .message.content import File, Photo, Video, SharedItem


class Chat:
    '''A list of messages'''
    _datasource: str
    messages: List[Message]
    participants: Set[str]

    def __init__(self, datasource):
        self._datasource = datasource
        message_files = [
            x for x in os.listdir(self._datasource) if re.match(r'message_\d+\.json', x)
        ]
        for message_file in message_files:
            with open(message_file, 'r') as data:
                chat_json = json.load(data.read())
                self.participants.update([x['name'] for x in chat_json['participants']])
                self.messages.append([Message(x) for x in chat_json['messages']])
        self.messages.sort(key=operator.attrgetter('timestamp'))

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
