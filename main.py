import os 
from pathlib import Path
import shutil
from functions import is_audio, is_image, is_video
from utils import folder_file_maps

# Change current directory to the target directory
try:
    target_directory = "/home/mehdirt/Downloads" #TODO: Change it to input
    os.chdir(target_directory)
except FileNotFoundError:
    print("The Path doesn't exist!")

# Getting the available files
files = [fl for fl in os.listdir() if os.path.isfile(fl)]
# 
for file in files:
    if is_audio(file):
        Path('Audios').mkdir(exist_ok=True)
        shutil.move(file, "./Audios")
            




# print(os.path.join('usr', 'bin', 'spam'))
# print(Path('usr').joinpath('bin').joinpath('spam'))