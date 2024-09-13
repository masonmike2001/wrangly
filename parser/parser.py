import shutil

from PIL import Image
import os


def parser(wd):
    # Parses through the working dir recursively, forming a list of all paths and all img's
    print("***********************************************")
    print("*****************Information*******************")
    print("Path:", wd)
    dirIsValid(wd)
    img_paths = []
    dir_paths = []
    for root, dirs, files in os.walk(wd):
        # print(f'Current Path: {root}')
        # print(f'Subdirectories: {dirs}')
        # print(f'Files: {files}')
        # print('--------------')
        for directory in dirs:
            dir_paths.append(root + "\\" + directory)
        for file in files:
            if file.endswith(('.jpg', '.png', '.jpeg')):
                img_paths.append(root + "\\" + file)
    # print(f"img{img_paths}");
    # print(f"dir{dir_paths}");
    print(f'Image count: {len(img_paths)}')
    print(f'Directory count: {len(dir_paths)}')
    while True:
        print("----------------------------------------------")
        print("Successfully traversed the directory. Ready to start organizing?")
        print("(1) Yes")
        print("(2) No")
        print("----------------------------------------------")
        choice = int(input("Selection: "))
        if choice == 1:
            organizer(img_paths, dir_paths)
        elif choice == 2:
            return


def organizer(img_paths, dir_paths):
    j = 0
    for img in img_paths:
        j += 1
        im = Image.open(img)
        im.show()

        print(f"***************Image {j} out of {len(img_paths)}********************")
        # print("(1) Search for dir")
        # print("(2) Autotag")
        # print("(3) Save progress and return")
        #
        # choice = int(input("Selection: "))
        # if choice == 1:
        results_present = False
        path = None
        imgName = im.filename.rsplit('\\', 1)[-1]

        while not results_present:
            search = input(f"Search for a directory to move <{imgName}> or \"exit\":")
            if search.lower() == exit:
                break
            # Traverses all dir paths
            res = [i for i in dir_paths if search.lower() in i.rsplit('\\', 1)[-1].lower()]
            print("---------------------------RESULTS---------------------------")
            for i in range(0, len(res)):
                if i > 5:
                    break
                dir_name = res[i].rsplit('\\', 1)[-1]
                print(f"({i + 1}): {dir_name}")
            path = res
            if len(res) != 0:
                results_present = True
            else:
                print("No results...")
                break
            print("-------------------------------------------------------------")
            dest = input(f"Which directory would you like to move <{imgName}>:")
            # move img to res dest
            test = (path[int(dest) - 1] + "\\" + im.filename.rsplit('\\', 1)[-1])
            print(f"Moving {img} to {test}:")
            shutil.move(img, test)
        # elif choice == 2:
        #     # To do
        #     return
        # elif choice == 3:
        #     return
        # else:
        #     print("Invalid choice. Please try again.")
        #     return
        # Opens image, and searches dir array for user input terms
        #


def dirIsValid(wd):
    return True
