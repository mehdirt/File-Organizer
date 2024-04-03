import os
from pathlib import Path
import shutil
from utils import folder_file_maps


def get_file_type(file: str) -> str: #! New
    """Return corresponding folder name to the file."""
    
    file_extension = Path(file).suffix
    for key in folder_file_maps:
        if file_extension in folder_file_maps[key]:
            return key
    raise Exception("This type of file is not supported!")

def transfer(folder_name: str, file: str) -> None:
    """Create a folder and transfer the file into it."""

    path = Path(folder_name)
    # Check if the file exists in the folder
    if not path.joinpath(file).is_file():
        path.mkdir(exist_ok=True)
        shutil.move(file, path.absolute())
    else:
        # Remove the file if it already exists
        os.remove(file)

def add_new_item(folder_name: str, file_ext: str) -> None: #! New
    """Add new extension to the given folder name."""
    
    folder_file_maps[folder_name].add(file_ext)
    print("Done!")

