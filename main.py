import json
import time

import config_files.config as config
from assistant.assistant import Assistant
from assistant.status import Status

jarvis = Assistant()
user_input = ""

while 'verlassen' not in user_input:
    user_input = input("[USER]: ")
    print(jarvis.message_and_response(user_input))