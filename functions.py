import os
from pathlib import Path
import shutil
from utils import folder_file_maps


def is_audio(file: str) -> bool:
    """Return True if the file is an audio."""
    
    file = Path(file)
    return file.suffix in folder_file_maps['Audios']

def is_video(file: str) -> bool:
    """Return True if the file is a video."""
    
    file = Path(file)
    return file.suffix in folder_file_maps['Videos']

def is_image(file: str) -> bool:
    """Return True if the file is an image."""
    
    file = Path(file)
    return file.suffix in folder_file_maps['Images']

def is_screenshot(file: str) -> bool:
    """Return True if the file is a screenshot."""

    file = Path(file)
    return file.suffix in folder_file_maps['Videos'] and 'screenshot' in file.stem.lower()

def transfer(folder_name: str, file: str) -> None:
    """Create the folder and transfer the file into it."""

    path = Path(folder_name)
    # Check if the file exist in the folder
    if not path.joinpath(file).is_file():
        path.mkdir(exist_ok=True)
        shutil.move(file, f"./{folder_name}")
    else:
        # Remove the file if it already exists
        os.remove(file)