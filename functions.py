import os
from pathlib import Path
import shutil
from utils import folder_file_maps


def organize():
    """Organize existing files on the given path."""

    # Take target path and change the current directory
    change_to_terget_path()
    # Get the available files
    files = [fl for fl in os.listdir() if os.path.isfile(fl)]
    # Create folders and move files
    for file in files:
        try:
            # Finding the corresponding folder name to the file extension
            folder = get_file_type(file)
        except Exception as err:
            print(err)
            print("Add the extinsion along with the related folder name using option-2, then reorganize.")
            continue
        # Moving the file into related folder
        transfer(folder, file)

def change_to_terget_path() -> None:
    """Get target location from user and change directory to the given path."""

    while True:
        try:
            path = input("Enter the target path for organizing: ").strip() 
            os.chdir(path)
            break
        except FileNotFoundError:
            print("This path doesn't exist!")

def get_file_type(file: str) -> str: 
    """Return corresponding folder name to the file."""
    
    file_extension = Path(file).suffix
    for key in folder_file_maps:
        if file_extension in folder_file_maps[key]:
            return key
    raise Exception(f"'{file_extension}' files are not supported!")

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

def add_new_item(folder_name: str, file_ext: str) -> None:
    """Add new extension to the given folder name."""
    
    folder_file_maps[folder_name].add(file_ext)
    print("Done!")

