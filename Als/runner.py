#!/usr/bin/env python
import pathlib
import sys
import os

from __init__ import __version__, __author__, __package__, __description__, __authorlinks__, __packagelinks__
from tree import DirectoryTree
from colors import Colors
from permissions import finder
from ls import ls

def main():
    helper = ["-h", "--help"]
    version = ["-v", "--version"]
    tree = ["-t", "--tree"]
    dironly = ["-d", "--dironly"]
    color = ["-c", "--color"]
    permission = ["-p", "--permissions"]
    args = sys.argv
    helpmessage = f"""
{__package__} v{__version__}

{__description__}

usage: myprogram.py [-h] [--foo FOO]

optional arguments:
 -h, --help         show this help message and exit
 -v, --version      show package's version and exit
 -t, --tree         use "tree" module of "Als"

extension arguments:
 -d, --dironly      set "tree" module to "directory only"
 -c, --color        set "ls" module to "show colored" [uses ANSII Escape color codes]
 -p, --permissions  set "ls" module to "show permissions"

{__packagelinks__}
{__authorlinks__}
"""
    if len(args) < 2:
        ls(color=False, permissions=False)
    elif len(args) > 3:
        print("Max Arguments --> 3")
        sys.exit()
    else:
        if args[1] in version and len(args) == 2:
            print(f"{__package__} v{__version__}")
        elif args[1] in helper and len(args) == 2:
            print(helpmessage)
        elif args[1] in tree and len(args) == 3:
            if args[2] in dironly:
                treeGenerator(os.getcwd(), True)
            else:
                print(f"only {dironly} is optional arguments for {tree}")
                sys.exit()
        elif args[1] in tree and len(args) == 2:
            treeGenerator(os.getcwd(), False)
        elif args[1] in color and len(args) == 3:
            if args[2] in permission:
                ls(color=True, permissions=True)
            else:
                print(f"only {permission} is optional arguments for {color}")
                sys.exit()
        elif args[1] in color and len(args) == 2:
                ls(color=True, permissions=False)
        elif args[1] in permission and len(args) == 3:
            if args[2] in color:
                ls(color=True, permissions=True)
            else:
                print(f"only {color} is optional arguments for {permission}")
                sys.exit()
        elif args[1] in permission and len(args) == 2:
            ls(color=False, permissions=True)

def treeGenerator(path, dir_only=False):
    tree = DirectoryTree(path, dir_only)
    tree.generate()
