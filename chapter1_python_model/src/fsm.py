from enum import Enum, auto

class AITLState(Enum):
    IDLE = auto()
    STARTUP = auto()
    RUN = auto()
    FAULT = auto()
