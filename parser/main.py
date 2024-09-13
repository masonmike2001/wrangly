from sys import argv

from parser import parser


def main():
    # imports command line argument for directory
    while True:
        print("**********************************************")
        print("Welcome to Wrangly! Please select an option:")
        print("(1) Traverse the directory and begin a session")
        print("(2) Restore a previous session")
        print("(3) Exit without saving")
        print("**********************************************")
        choice = int(input("Selection: "))
        if choice == 1:
            parser(argv[1])
        elif choice == 2:
            # To do
            return
        elif choice == 3:
            return
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
