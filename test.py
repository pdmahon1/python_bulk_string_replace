#! /bin/env python3

import rename

import os
import shutil
import subprocess
import sys

from stat import *

#to be imported as a module, if needed
TEST_DIR_NAME = "_test_directory"

def get_test_directory_name():
    return TEST_DIR_NAME

def get_old_substr():
    return "CHANGE-ME"

def get_new_substr():
    return "CHANGED"


def set_argv(args):
    sys.argv = args


def remove_existing_path(path):
    if os.path.exists(path):
        shutil.rmtree(path, ignore_errors=True)


def modify_new_dir_permissions(path:str):
    subprocess.run(['chmod', '777', path])


def create_new_test_dir(new_dir_name):
    current_dir = os.getcwd()
    original_test_dir = os.path.join(current_dir, get_test_directory_name())
    modified_test_dir = os.path.join(current_dir, new_dir_name)

    remove_existing_path(modified_test_dir)
    shutil.copytree(original_test_dir, modified_test_dir)


def setup_and_run(dirname, old_substr, new_substr, with_recursion = False):
    new_args = ["filename",  old_substr, new_substr, "./"]
    if with_recursion:
        new_args.insert(1, "-r")
    
    set_argv(new_args)
    create_new_test_dir(dirname)
    rename.run()
    # TODO walk the tree and verify that no filenames contain [old_substr]


def run():
    old = get_old_substr()
    new = get_new_substr()
    
    setup_and_run("copy_no_recursion", old, new, False)
    setup_and_run("copy_with_recursion", old, new, True)

if __name__ == "__main__":
    run()
