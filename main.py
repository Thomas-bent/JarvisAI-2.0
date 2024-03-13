from IO.input import Input
from IO.output import Output
from assistant.assistant import Assistant
from config_files import config

#####################################################################################
#   AI ASSISTANT
#   VERSION 2.0.0
#   BY THOMAS BENTLOHNER
#####################################################################################

jarvis = Assistant()
output = Output()
user_input = Input()
text = ""

while 'verlassen' not in text:

    text = user_input.audio_input()
    print(f"[USER] { text }")
    ans = jarvis.message_and_response(text)
    output.interact(ans)
    print(f"[{config.assistant.NAME}] { ans }")
    output.play()
