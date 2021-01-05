'''Parse chat content'''


import os
import re
from typing import List
from messenger_analysis.util.search import search_files
from .chat import Chat


def parse_chats(datasource: str) -> List[Chat]:
    '''Retrieve all chats in the datasource'''
    message_files = [x for x in search_files(datasource) if re.search(r'message_\d+\.json$', x)]
    chat_dirs = {m_file[:m_file.rindex(os.path.sep)] for m_file in message_files}
    return list(map(Chat, chat_dirs))
