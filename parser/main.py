from sys import argv

from parser import parser
def main():
    print("Hello World!")
    wd = argv[1]
    # imports command line argument for directory
    parser(wd)

if __name__ == "__main__":
    main()

