import openai
import pygame
import config_files.config as config


class Output:
    """
    Class for text-to-speech transcription of the AI assistants responses.
    """

    def __init__(self):
        self.output_id = config.tts.OUTPUT_START_ID

    def interact(self, message: str) -> None:
        """
        Converts a string into an audio file.
        :param message: The message to convert.
        """
        response = openai.audio.speech.create(
            model=config.tts.MODEL,
            voice=config.tts.VOICE,
            input=message
        )
        response.stream_to_file(f"{config.media.OUTPUT_FOLDER}/output_{self.output_id}.mp3")
        self.output_id += 1

    def play(self) -> None:
        """
        Plays the latest audio file in config.media.OUTPUT_FOLDER.
        """
        # print(f"{ config.media.output_folder }/output_{self.output_id - 1}.mp3")
        pygame.mixer.init()
        pygame.mixer.music.load(f"{ config.media.OUTPUT_FOLDER }/output_{self.output_id - 1}.mp3")
        pygame.mixer_music.play()
