#! /bin/env python3

import os
import re
import sys
from stat import *
from test import TEST_DIR_NAME as test_dir

DEBUG = False

def LOG(output, force = False) -> None:
    if DEBUG or force:
        print(output)

def abs_path(file:str, path:str) -> str:
    return os.path.join(path, file)


def has_permission(path:str) -> bool:
   return os.access(path, os.W_OK)


def rename(old_path, new_path):
    LOG("CHANGING FILENAMES")
    LOG("\tOld Path: " + old_path)
    LOG("\tNew Path: " + new_path)
    os.rename(old_path, new_path)


def change_filename(filename: str, path: str, from_str: str, to_str: str) -> None:
    new_filename = re.sub(from_str, to_str, filename)
    if new_filename == filename:
        return
    
    #a substring replacement was made. Change the file name in the filesystem
    old_path = abs_path(filename, path)
    new_path = abs_path(new_filename, path)
    rename(old_path, new_path)


def scan_and_rename_files(recurse: bool, from_str:str , to_str:str, path:str) -> None:
    LOG("IN RENAME_FILES")
    for dir_item in os.listdir(path):
        item_path = abs_path(dir_item, path)
        mode = os.lstat(item_path).st_mode
        LOG("\tItem Path = " + item_path + "\n\t\tIs DIR? " + str(S_ISDIR(mode)) + "\n\t\tIs REG? " + str(S_ISREG(mode)))
        
        if not has_permission(item_path) or dir_item == "_test_directory":
            # the _test_directory/ must not be altered, even if this user can write to it
            continue

        if S_ISDIR(mode) and recurse:
            scan_and_rename_files(recurse, from_str, to_str, abs_path(dir_item, path))
        
        if S_ISDIR(mode) or S_ISREG(mode):
            change_filename(dir_item, path, from_str, to_str)       


def check_arg_length_exception(args:list) -> None:
    if len(args) < 3:
        raise OSError("Program command did not contain enough arguments")
    elif len(args) > 3:
        raise OSError("Program command contains too many arguments")
    

def get_arguments():
    args = list(sys.argv) #remove filename
    args.pop(0)
    is_recursive = False

    if args[0] == "-r":
        is_recursive = True
        args.pop(0)

    check_arg_length_exception(args)

    from_str = args[0]
    to_str = args[1]
    path = os.path.expanduser(args[2])
    LOG("get_options = [" + ", ".join([str(is_recursive), from_str, to_str, path]) + "]")
    return is_recursive, from_str, to_str, path


def run():
    LOG("Running rename.py")
    is_recursive, from_str, to_str, path = get_arguments()
    #start_loc = os.scandir(start_loc)
    scan_and_rename_files(is_recursive, from_str, to_str, path)
    


if __name__ == "__main__":
    run()