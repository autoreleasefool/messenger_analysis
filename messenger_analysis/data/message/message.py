'''Common properties and operations for messages.'''


from enum import Enum, auto
from typing import List
from content import Photo, Video, SharedItem, File, Reaction


class MessageType(Enum):
    '''Types of messages'''
    Generic = auto()
    Share = auto()
    Call = auto()


class Message:
    '''A single message and its contents'''
    sender: str
    timestamp: int
    content: str
    message_type: MessageType
    unrecognized_properties: List[str]

    has_media: bool
    photos: List[Photo] = []
    videos: List[Video] = []

    files: List[File] = []
    shares: List[SharedItem] = []
    reactions: List[Reaction] = []

    def __init__(self, message_json):
        # Common properties
        self.sender = message_json['sender_name']
        self.timestamp = message_json['timestamp_ms']
        self.content = message_json['content']
        self.message_type = MessageType[message_json['type']]
        self.unrecognized_properties = []

        # Media
        if 'photos' in message_json:
            self.photos = [Photo(self.sender, x) for x in message_json['photos']]
        if 'videos' in message_json:
            self.videos = [Video(self.sender, x) for x in message_json['videos']]
        self.has_media = self.photos or self.videos

        # Share
        if self.message_type is MessageType.Share:
            self.shares = [SharedItem(self.sender, x) for x in message_json['share']]

        # Other
        if 'files' in message_json:
            self.files = [File(self.sender, x) for x in message_json['files']]
        if 'reactions' in message_json:
            self.reactions = [Reaction(x) for x in message_json['reactions']]
