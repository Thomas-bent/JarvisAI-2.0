# JarvisAI

Current version: 2.0.0

## Guide

### Installation

The installation process is as follows:

1. Download the Repository.
2. Run the ```main.py``` file via ```python3 main.py```
3. There are packages missing? Install them with ```pip3 install <package-name>```. Known requirements are
    - speechrecognition
    - opencv-python
    - openai
    - pyaudio
    - pygame
4. Create a file ```api_keys.py``` inside the ```/config_files``` folder with the content:

```python3
OPENAI_API_KEY = "<API-KEY>"
```

If you encounter problems during the installation process try creating a virtual environment.

### Customization

#### Custom Functions

You can write your own functions inside the ```/assistant/functions.py``` file. Then add an entry to the
```FunctionNames``` enum inside ```/assistant/function_names.py```. Now you can add the function to the
```get_output``` function inside ```/assistant/assistant.py```. Simply create a new case in the format

```python3
elif function_name == FunctionNames.YOUR_FUNCTION
return functions.your_function(args['your_arg'], args['your_arg...'])
```

At last, add the function to the tools. Therefore you have to create an object in the ```/config_files/config.py```
file. Write it into ```assistant.TOOLS``` in the following format:

```json
{
  "type": "function",
  "function": {
    "name": "<function name>",
    "description": "<function description>",
    "parameters": {
      "type": "object",
      "properties": {
        "<parameter_name>": {
          "type": "<parameter_type>",
          "description": "<parameter_description>"
        }
      },
      "required": [
        "<required_parameter>"
      ]
    }
  }
}
```

#### Custom Settings

In the ```/config_files/config.py``` file, you can also change various other settings. A little overview:

| Section     | Name                  | Description                                                                   | Default                      | Restrictions                        |
|-------------|-----------------------|-------------------------------------------------------------------------------|------------------------------|-------------------------------------|
| ```media``` | ```OUTPUT_FOLDER```   | The folder where all the Speech output files are stored in.                   | ```/media/speechOutput/```   | Must be a valid folder.             |
| ```media``` | ```IMAGE_FOLDER```    | The folder where all the Images are stored in.                                | ```/media/images/```         | Must be a valid folder.             |
| ```media``` | ```GENERATED_FILES``` | The folder where all the files and folders that Jarvis Creates are stored in. | ```/media/generatedFiles/``` | Must be a valid folder.             |
| ```media``` | ```AUDIO_FOLDER```    | The folder where all the accessible audio files are stored in.                | ```/media/audio/```          | Must be a valid folder.             |
| ```tts```   | ```MODEL```           | The TTS model which will be used to create speech for Jarvis.                 | ```tts```                    | ```tts-1``` or ```tts-1-hd```       |
| ```tts```   | ```LANGUAGE```        | The TTS models language (currently not in use).                               | ```de-DE```                  | Every language in valid format.     |
| ```tts```   | ```VOICE```           | The TTS models voice.                                                         | ```alloy```                  | One of the six valid OpenAI voices. |
| ```tts```   | ```OUTPUT_START_ID``` | The index of the first speech output file.                                    | 0                            | Must be an integer.                 |

