'''Structure of common message content.'''


from typing import Dict, Any
from messenger_analysis.util.validation import validate_keys

class Photo:
    '''A photo sent to the chat members'''
    sender: str
    location: str
    timestamp: int

    def __init__(self, sender: str, photo_json: Dict[str, Any]):
        self.sender = sender
        self.location = photo_json['uri']
        self.timestamp = photo_json['creation_timestamp']
        validate_keys('photo', set(photo_json.keys()), set(('uri', 'creation_timestamp')))


class Gif:
    '''A gif sent to the chat members'''
    sender: str
    location: str

    def __init__(self, sender: str, gif_json: Dict[str, Any]):
        self.sender = sender
        self.location = gif_json['uri']
        validate_keys('gif', set(gif_json.keys()), set(['uri']))


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
        validate_keys('video', set(video_json.keys()), set(('uri', 'creation_timestamp', 'thumbnail')))


class SharedItem:
    '''An item shared to the chat.'''
    sender: str
    uri: str

    def __init__(self, sender: str, share_json: Dict[str, Any]):
        self.sender = sender
        self.uri = share_json['link']
        validate_keys('share', set(share_json.keys()), set(['link']))


class File:
    '''A file sent to the chat members.'''
    sender: str
    uri: str
    timestamp: int

    def __init__(self, sender: str, file_json: Dict[str, Any]):
        self.sender = sender
        self.uri = file_json['uri']
        self.timestamp = file_json['creation_timestamp']
        validate_keys('file', set(file_json.keys()), set(('uri', 'creation_timestamp')))


class Reaction:
    '''A reaction to a message.'''
    sender: str
    reaction: str

    def __init__(self, reaction_json):
        self.sender = reaction_json['actor']
        self.reaction = reaction_json['reaction']
        validate_keys('reaction', set(reaction_json.keys()), set(('actor', 'reaction')))


class Sticker:
    '''A sticker sent to the chat members'''
    sender: str
    location: str

    def __init__(self, sender: str, sticker_json: Dict[str, Any]):
        self.sender = sender
        self.location = sticker_json['uri']
        validate_keys('gif', set(sticker_json.keys()), set(['uri']))
