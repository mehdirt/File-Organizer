import os 
from pathlib import Path
import shutil
from functions import is_audio, is_image, is_video, is_screenshot, transfer

# Change current directory to the target directory
try:
    target_directory = "/home/mehdirt/Downloads" #TODO: Change it to input
    os.chdir(target_directory)
except FileNotFoundError:
    print("The Path doesn't exist!")

# Getting the available files
files = [fl for fl in os.listdir() if os.path.isfile(fl)]

# Create folders and move files
try:
    for file in files:
        if is_audio(file):
            transfer('Audios', file)
        elif is_video(file):
            transfer('Videos', file)
        elif is_image(file):
            if is_screenshot(file):
                transfer('Screenshots', file)
            else:
                transfer('Images', file)
except shutil.Error as err:
    print(err)

# print(os.path.join('usr', 'bin', 'spam'))
# print(Path('usr').joinpath('bin').joinpath('spam'))