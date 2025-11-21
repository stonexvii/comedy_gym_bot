import os
from enum import Enum


class Path(Enum):
    MESSAGES = 'messages'
    START_COMMAND = os.path.join('messages', 'start')
    ABOUT = os.path.join('messages', 'about')
    REGISTERED = os.path.join('messages', 'registered')
