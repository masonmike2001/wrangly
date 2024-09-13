import shutil

from PIL import Image

import os


def parser(wd, favorite_paths):
    # Parses through the working dir recursively, forming a list of all paths and all img's
    print("***********************************************")
    print("*****************Information*******************")
    print("Path:", wd)
    dirIsValid(wd)
    img_paths = []
    dir_paths = []
    files = os.listdir(wd)
    for file in files:
        if str(file).endswith(('.jpg', '.png', '.jpeg')):
            img_paths.append(wd + "\\" + file)
        elif not str(file).endswith('.'):
            dir_paths.append(wd + "\\" + file)
    print(dir_paths)
    print(img_paths)

    print(f'Image count: {len(img_paths)}')
    print(f'Directory count: {len(dir_paths)}')
    organizer(img_paths, dir_paths, favorite_paths, wd)


def organizer(img_paths, dir_paths, favorite_paths, wd):
    j = 0
    for img in img_paths:
        j += 1
        im = Image.open(img)
        im.show()
        print(f"***************Image {j} out of {len(img_paths)}********************")
        results_present = False
        path = None
        imgName = im.filename.rsplit('\\', 1)[-1]
        k = 0

        print("(0) EXIT BACK TO PREVIOUS SCREEN")
        for favorite in favorite_paths:
            print(f"({k + 1}) {favorite}")
            k += 1
        dest = input(f"Which favorite directory would you like to move <{imgName}>:")
        # move img to res dest
        if dest == 0:
            break
        else:
            test = (favorite_paths[int(dest) - 1] + "\\" + im.filename.rsplit('\\', 1)[-1])
            print(f"Moving {img} to {test}:")
            shutil.move(img, test)


def dirIsValid(wd):
    return True


def parse_directory(wd, return_dir):
    # Returns directories exclusively or all depending on return_dir bool
    output = []
    files = os.listdir(wd)
    for file in files:
        if str(file).endswith(('.jpg', '.png', '.jpeg')):
            # if img, only save if return_dir is false
            if not return_dir:
                output.append(wd + "\\" + file)
                break
        elif not str(file).endswith('.'):
            output.append(wd + "\\" + file)
    return output
