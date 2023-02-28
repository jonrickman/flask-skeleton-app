import sys
import os
import shutil

def main():
    src_root = os.getcwd()

    # if params given then use them
    if len(sys.argv) == 3:
        print("Using passed in arguments")
        # get params for copy from args
        dest_root = sys.argv[1]
        proj_name = sys.argv[2]

        return copy_files(src_root, dest_root, proj_name)

    # if both params not given, get new params
    print("Incorrect number of arguments passed in")
    dest_root = input("Input destination root path: ")
    proj_name = input("Input project name: ")

    return copy_files(src_root, dest_root, proj_name)

def copy_files(src_root, dest_root, proj_name):

    # build the src path to copy from
    src = os.path.join(src_root, "skeleton_files")
    # build the dest path to copy to
    dest = os.path.join(dest_root, proj_name)

    # if path already exists items must be deleted first
    if os.path.exists(dest):
        print(f"Deleting files from existing path {dest}")
        shutil.rmtree(dest)

    # perform copy
    print(f"copying {src} into {dest}")
    shutil.copytree(src, dest)
    print(f"Done!")

if __name__ == "__main__":
    print("Help: python3 main.py target_root proj_name")
    main()