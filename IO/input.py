import speech_recognition as sr


class Input:
    def __init__(self):
        self.akt_input = ''
        self.r = sr.Recognizer()

    def audio_input(self):
        while 1:
            try:
                with sr.Microphone() as source:
                    self.r.adjust_for_ambient_noise(source, duration=0.5)
                    audio = self.r.listen(source)
                    text = self.r.recognize_google(audio, language='de')
                    if "jarvis" in text.lower():
                        return text
            except sr.RequestError as e:
                print("Could not request results fro; {0}".format(e))
            except sr.UnknownValueError:
                print("Unknown Error!")
