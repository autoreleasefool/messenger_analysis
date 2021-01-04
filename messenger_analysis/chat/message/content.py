'''Structure of common message content.'''


from typing import Dict, Any


class Photo:
    '''A photo sent to the chat members'''
    sender: str
    location: str
    timestamp: int

    def __init__(self, sender: str, photo_json: Dict[str, Any]):
        self.sender = sender
        self.location = photo_json['uri']
        self.timestamp = photo_json['creation_timestamp']


class Video:
    '''A video sent to the chat members.'''
    sender: str
    location: str
    timestamp: int
    thumbnail_uri: str

    def __init__(self, sender: str, video_json: Dict[str, Any]):
        self.sender = sender
        self.location = video_json['uri']
        self.timestamp = video_json['creation_timestamp']
        self.thumbnail_uri = video_json['thumbnail']['uri']


class SharedItem:
    '''An item shared to the chat.'''
    sender: str
    uri: str

    def __init__(self, sender: str, share_json: Dict[str, Any]):
        self.sender = sender
        self.uri = share_json['link']


class File:
    '''A file sent to the chat members.'''
    sender: str
    uri: str
    timestamp: int

    def __init__(self, sender: str, file_json: Dict[str, Any]):
        self.sender = sender
        self.uri = file_json['uri']
        self.timestamp = file_json['creation_timestamp']


class Reaction:
    '''A reaction to a message.'''
    sender: str
    reaction: str

    def __init__(self, reaction_json):
        self.sender = reaction_json['actor']
        self.reaction = reaction_json['reaction']
