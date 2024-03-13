from enum import Enum


class Status(Enum):
    QUEUED = 'queued'
    COMPLETED = 'completed'
    REQUIRES_ACTION = 'requires_action'
