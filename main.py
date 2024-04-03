import os 
from functions import get_file_type, transfer, add_new_item

# Change current directory to the target directory
try:
    print("Welcome to the program :)")
    # Get the target location
    target_directory = input("please enter the target location for organizing: ").strip() #"/home/mehdirt/Downloads" 
    os.chdir(target_directory)

except FileNotFoundError:
    print("The Path doesn't exist!")

# Getting the available files
files = [fl for fl in os.listdir() if os.path.isfile(fl)]

# Create folders and move files
for file in files:
    try:
        # Finding the corresponding folder name to the file extension
        folder = get_file_type(file)

    except Exception as err:
        print(err)
        print("You can add new extension along with a folder.")
        #TODO: Add this function -> add_new_item()
    # Moving the file into related folder
    transfer(folder, file)

# print(os.path.join('usr', 'bin', 'spam'))
# print(Path('usr').joinpath('bin').joinpath('spam'))