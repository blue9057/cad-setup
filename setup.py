#!/usr/bin/env python3

import os
import shutil
import subprocess


def get_current_path():
    return os.path.dirname(os.path.abspath(__file__))

def install_bashrc():
    print(get_current_path())

def main():
    install_bashrc()

if __name__ == '__main__':
    main()
