import os

from config_files import config
from utils.pathmaker import create_path, create_priority_path
from backend import linker
import cv2


####################################################################
#   Functions that the assistant can use.
####################################################################

def capture_image(filename: str) -> str:
    """
    Captures an image and saves it to the config.media.IMAGE_FOLDER.
    :param filename: The name of the picture file.
    :return: The path to the file.
    """
    path = create_path(config.media.image_folder, filename)
    cam = cv2.VideoCapture(0)
    result, image = cam.read()
    cv2.imwrite(path.resolve(), image)
    return str(path)


def create_file(filename: str, path: str) -> str:
    """
    Creates a new file in the given directory.
    :param filename: The name of the new file.
    :param path: The path to the file. If it is a relative path, the root will be config.media.GENERATED_FILES
    :return: The location of the new file.
    """
    location = create_priority_path(path, config.media.GENERATED_FILES, filename).resolve()
    try:
        file = open(location, 'x')
        file.close()
    except FileNotFoundError:
        return 'File could not be created!'
    return location


def create_folder(folder_name: str, path: str) -> str:
    """
    Creates a folder in the given directory.
    :param folder_name: Name of the new folder.
    :param path: Path to the folder, if not absolute it is relative to config.media.GENERATED_FILES
    :return:
    """
    location = create_priority_path(path, config.media.GENERATED_FILES, folder_name).resolve()
    if not os.path.exists(location):
        os.makedirs(location)
    return location


def write_file(filename: str, content: str, path: str) -> str:
    """
    Writes to a file with the given name and path. If path is relative, it will be viewed as relative to
    config.media.GENERATED_FILES.
    :param filename: The name of the file.
    :param content: The content to write into the file.
    :param path: Absolute or relative path to the file.
    :return: The absolute Path to the file.
    """
    location = create_priority_path(path, config.media.GENERATED_FILES, filename).resolve()
    with open(location, 'w') as file:
        file.write(content)
        file.close()
    return location


def console_command(command: str) -> str:
    """
    Executes a command on the CLI.
    :param command: The command to execute.
    :return: 'executed'.
    """
    os.system(command)
    return 'executed'


def get_contacts() -> list[str]:
    return linker.get('/contacts').json()
