from enum import Enum


class FunctionNames(Enum):
    """
    All names to the functions which the assistant can use.
    """
    CAPTURE_IMAGE = 'capture_image'
    CREATE_FILE = 'create_file'
    CREATE_FOLDER = 'create_folder'
    WRITE_FILE = 'write_file'
    CONSOLE_COMMAND = 'console_command'
