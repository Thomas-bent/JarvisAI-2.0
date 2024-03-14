import pathlib
import platform

from config_files import api_keys
from config_files.struct import Struct as Section

from utils.pathmaker import create_path

# Sets the BASE_PATH to the Project directory
BASE_PATH = str(pathlib.Path(__file__).parent.parent.resolve())

# Sets ROOT to the root folder of the os for checks
ROOT = ''
if platform.system() == "Windows":
    ROOT = 'C:'
else:
    ROOT = 'home'

# API keys setup
OPENAI_API_KEY = api_keys.OPENAI_API_KEY

# Media Folder setup
media = Section("media folder paths")
media.OUTPUT_FOLDER = create_path(BASE_PATH, "/media/speechOutput").resolve()
media.IMAGE_FOLDER = create_path(BASE_PATH, "/media/images").resolve()
media.GENERATED_FILES = create_path(BASE_PATH, "/media/generatedFiles").resolve()
media.AUDIO_FOLDER = create_path(BASE_PATH, "/media/audio").resolve()

# Text-To-Speech settings setup
tts = Section("tts configs")
tts.MODEL = "tts-1"
tts.LANGUAGE = "de-DE"
tts.VOICE = "alloy"
tts.OUTPUT_START_ID = 0

# Assistant Settings setup
assistant = Section("assistant configs")
assistant.NAME = "Jarvis"
assistant.INSTRUCTIONS = '''
You are a personal assistant. You are used in technical areas like computer science, 
math and mechanical engineering. You will ask him if you can do something for him. Du sprichst deutsch.
'''
assistant.MODEL = "gpt-4-turbo-preview"
assistant.TAKT = 0.1
assistant.TOOLS = [
    {
        "type": "code_interpreter"
    }, {
        "type": "function",
        "function": {
            "name": "capture_image",
            "description": "Captures an image with the camera.",
            "parameters": {
                "type": "object",
                "properties": {
                    "file-name": {
                        "type": "string",
                        "description": "the name of the image."
                    }
                },
                "required": [
                    "file-name"
                ]
            }
        }
    }, {
        "type": "function",
        "function": {
            "name": "create_file",
            "description": "creates a new file.",
            "parameters": {
                "type": "object",
                "properties": {
                    "file-name": {
                        "type": "string",
                        "description": "The name of the new file."
                    },
                    "path": {
                        "type": "string",
                        "description": "The path that leads to the new file."
                    }
                },
                "required": [
                    "file-name",
                    "path"
                ]
            }
        }
    }, {
        "type": "function",
        "function": {
            "name": "create_folder",
            "description": "Creates a new folder.",
            "parameters": {
                "type": "object",
                "properties": {
                    "folder-name": {
                        "type": "string",
                        "description": "The name of the new folder."
                    },
                    "path": {
                        "type": "string",
                        "description": "The path that leads to the new folder."
                    }
                },
                "required": [
                    "folder-name",
                    "path"
                ]
            }
        }
    }, {
        "type": "function",
        "function": {
            "name": "write_file",
            "description": "Writes the provided content into the provided file.",
            "parameters": {
                "type": "object",
                "properties": {
                    "file-name": {
                        "type": "string",
                        "description": "The name of the file that will be written into."
                    },
                    "content": {
                        "type": "string",
                        "description": "The content that will be written."
                    },
                    "path": {
                        "type": "string",
                        "description": "The path that leads to the file."
                    }
                },
                "required": [
                    "file-name",
                    "content",
                    "path"
                ]
            }
        }
    }, {
        "type": "function",
        "function": {
            "name": "console_command",
            "description": "Executes the provided command in the CLI.",
            "parameters": {
                "type": "object",
                "properties": {
                    "command": {
                        "type": "string",
                        "description": "The command that will be executed."
                    }
                },
                "required": [
                    "command"
                ]
            }
        }
    }
]

# Backend settings
backend = Section()
backend.PORT = 8000
backend.HOSTNAME = f"localhost:{backend.PORT}"
backend.URL = f"http://{backend.HOSTNAME}"
