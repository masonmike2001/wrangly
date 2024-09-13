import os
from sys import argv

from parser import parser, parse_directory


def main():
    favorite_paths = []
    wd = argv[1]
    while True:
        print("**********************************************")
        print("Welcome to Wrangly:")

        print("(1) Set favorite directories")
        print("(2) Traverse the directory and begin a session")
        print("(3) Choose another directory to organize")
        print("(4) Exit")
        print("**********************************************")
        choice = int(input("Selection: "))
        if choice == 1:
            # files holds the directories
            files = parse_directory(wd, True)
            k = 0
            for file in files:
                print(f"({k + 1}) {file}")
                k += 1
            print("(0) Return")
            selection = -1
            while selection != 0:
                selection = int(input("Which of these directories would you like to favorite: "))
                if selection == 0:
                    break
                else:
                    favorite_paths.append(files[int(selection) - 1])
                    print(f"{files[int(selection) - 1]} has been favorited")
                    print(favorite_paths)
        elif choice == 2:
            parser(wd, favorite_paths)
        elif choice == 3:
            print("Please type in the directory you'd like to organize"
                  "level higher.")
            files = parse_directory(wd, True)
            k = 0
            for file in files:
                print(f"({k + 1}) {file}")
                k += 1
            print("(-1) Go up one directory <../>")
            print("(0) Return")
            selection = -1
            while selection != 0:
                selection = int(input("Selection: "))
                if selection == 0:
                    break
                elif selection == -1:
                    wd = (wd.rsplit("\\", 1))[0]
                    break
                else:
                    wd = files[int(selection)]
                    print(f"{files[int(selection) - 1]} is the new path. Returning...")
                    break
        elif choice == 4:
            return
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
