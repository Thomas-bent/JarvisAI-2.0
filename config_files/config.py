import pathlib
from config_files.struct import Struct as Section
import sys

base_path = str(pathlib.Path(__file__).parent.parent.resolve())

# API keys
OPENAI_API_KEY = "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"

# Media Section
media = Section("media folder paths")
media.output_folder = base_path + "/media/speechOutput"
media.image_folder = base_path + "/media/images"
media.generated_files = base_path + "/media/generatedFiles"
media.audio_folder = base_path + "/media/audio"

# Text-To-Speech
tts = Section("tts configs")
tts.model = "tts-1"
tts.language = "de-DE"
tts.voice = "alloy"
tts.output_start_id = 0

# Assistant Settings
assistant = Section("assistant configs")
assistant.name = "Jarvis"
assistant.instructions = '''
    You are a personal assistant. You are used in technical areas like computer science, math and mechanical engineering. 
    You will ask him if you can do something for him. Du sprichst deutsch.
'''
assistant.model = "gpt-3.5-turbo-1106"
assistant.takt = 0.1
assistant.tools = [
    {
        "type": "code_interpreter"
    }
]
