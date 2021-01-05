'''Common properties and operations for messages.'''


from enum import Enum, auto
from typing import List, Optional, Set
from messenger_analysis.util.validation import validate_keys
from .content import Photo, Video, SharedItem, File, Reaction, Gif, Sticker


class MessageType(Enum):
    '''Types of messages'''
    Generic = auto()
    Share = auto()
    Call = auto()
    Unsubscribe = auto()
    Subscribe = auto()


class Message:
    '''A single message and its contents'''
    sender: str
    timestamp: int
    content: str
    message_type: MessageType
    call_duration: Optional[int] = None # pylint: disable=unsubscriptable-object

    has_media: bool
    photos: List[Photo] = []
    videos: List[Video] = []
    gifs: List[Gif] = []

    files: List[File] = []
    shares: List[SharedItem] = []
    reactions: List[Reaction] = []
    sticker: Optional[Sticker] = None # pylint: disable=unsubscriptable-object

    users: Set[str] = []

    def __init__(self, message_json):
        # Common properties
        self.sender = message_json['sender_name']
        self.timestamp = message_json['timestamp_ms']
        self.message_type = MessageType[message_json['type']]

        if 'content' in message_json:
            self.content = message_json['content']

        # Media
        if 'photos' in message_json:
            self.photos = [Photo(self.sender, x) for x in message_json['photos']]
        if 'videos' in message_json:
            self.videos = [Video(self.sender, x) for x in message_json['videos']]
        if 'gifs' in message_json:
            self.gifs = [Gif(self.sender, x) for x in message_json['gifs']]
        self.has_media = self.photos or self.videos or self.gifs

        # Share
        if 'share' in message_json:
            self.shares = [SharedItem(self.sender, message_json['share'])]

        # Other
        if 'files' in message_json:
            self.files = [File(self.sender, x) for x in message_json['files']]
        if 'reactions' in message_json:
            self.reactions = [Reaction(x) for x in message_json['reactions']]
        if 'sticker' in message_json:
            self.sticker = Sticker(self.sender, message_json['sticker'])
        if 'users' in message_json:
            self.users = {x['name'] for x in message_json['users']}
        if 'call_duration' in message_json:
            self.call_duration = message_json['call_duration']

        validate_keys(
            'message',
            set(message_json.keys()),
            set(('sender_name', 'timestamp_ms', 'type', 'content', 'photos', 'videos',
                'share', 'files', 'reactions', 'gifs', 'sticker', 'users', 'call_duration'))
        )
