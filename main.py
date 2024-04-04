import time
from functions import organize, add_new_item, show_map

#TODO: Make the printing better

def main() -> None:

    print("""Welcome to File Organizer 🔍\nOptions:
    1- Organize a Folder
    2- Add New Extension
    3- Show existed folder-file map
    4- exit""")
    while True:
        option = int(input("Choose an option to be performd: "))
        if option == 1:
            organize()
        elif option == 2:
            fldr_name, ext = input("Enter a folder name and a new extension to add (Example: Audios, .mp3 ): ").split(',')
            add_new_item(fldr_name, ext)
        elif option == 3:
            show_map()
        elif option == 4:
            print("Good Bye 👋")
            time.sleep(1.25)
            break

if __name__ == '__main__':
    main()
