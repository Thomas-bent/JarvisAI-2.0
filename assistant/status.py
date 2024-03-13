from enum import Enum

from config_files.struct import Struct as Section

Status = Section()
Status.QUEUED = 'queued'
Status.COMPLETED = 'completed'
Status.REQUIRES_ACTION = 'requires_action'
