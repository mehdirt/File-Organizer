import time
from functions import organize, add_new_item

#TODO: Make the printing better

def main() -> None:

    print("""Welcome to File Organizer 🔍\nOptions:
    1- Organize a Folder
    2- Add New Extension
    3- exit""")
    while True:
        option = int(input("Choose an option to be performd: "))
        if option == 1:
            organize()
        elif option == 2:
            add_new_item() #FIXME
        elif option == 3:
            print("Good Bye 👋")
            time.sleep(1.25)
            break

if __name__ == '__main__':
    main()
