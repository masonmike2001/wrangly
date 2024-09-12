import shutil

from PIL import Image
import os


def parser(wd):
    # Parses through the working dir recursively, forming a list of all paths and all img's
    print("Current working directory:", wd)
    dirIsValid(wd)
    img_paths = []
    dir_paths = []
    for root, dirs, files in os.walk(wd):
        print(f'Current Path: {root}')
        print(f'Subdirectories: {dirs}')
        print(f'Files: {files}')
        print('--------------')
        for directory in dirs:
            dir_paths.append(root + "\\" + directory)
        for file in files:
            if file.endswith(('.jpg', '.png', '.jpeg')):
                img_paths.append(root + "\\" + file)
    print(f"img{img_paths}");
    print(f"dir{dir_paths}");
    print(f'Image number: {len(img_paths)}')
    print(f'Dir number: {len(dir_paths)}')
    organizer(img_paths, dir_paths)


def organizer(img_paths, dir_paths):
    for img in img_paths:
        # Opens image, and searches dir array for user input terms
        #
        im = Image.open(img)
        im.show()

        results_present = False
        path = None
        imgName = im.filename.rsplit('\\', 1)[-1]

        while results_present == False:
            search = input(f"Search for a directory to store {imgName}:")
            # TODO error checking for search    directory.rsplit('\\', 1)
            # Traverses all dir paths
            res = [i for i in dir_paths if search.lower() in i.rsplit('\\', 1)[-1].lower()]
            print("---------------------------RESULTS---------------------------")
            for i in range(0, len(res)):
                if i > 20:
                    break
                dir_name = res[i].rsplit('\\', 1)[-1]
                print(f"({i}): {dir_name}")

            path = res
            if len(res) != 0:
                results_present = True
            else:
                print("No results...")
        print("-------------------------------------------------------------")
        dest = input("Enter the number of directory to move img to:")
        # move img to res dest
        test = (path[int(dest)] + "\\" + im.filename.rsplit('\\', 1)[-1])
        print(f"Moving {img} to {test}:")
        shutil.move(img, test)


def dirIsValid(wd):
    return True
