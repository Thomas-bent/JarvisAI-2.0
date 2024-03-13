import pathlib
import platform

from config_files import api_keys
from config_files.struct import Struct as Section
import sys

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
    You are a personal assistant. You are used in technical areas like computer science, math and mechanical engineering. 
    You will ask him if you can do something for him. Du sprichst deutsch.
'''
assistant.MODEL = "gpt-4-turbo-preview"
assistant.TAKT = 0.1
assistant.TOOLS = [
    {
        "type": "code_interpreter"
    }
]
