#!python3
#ls.py
"""
\"ls\" module for Als
"""

import os
from permissions import finder
from colors import Colors

def ls(color=False, permissions=False, path=os.getcwd()):
    lslist = os.listdir(path)
    for item in lslist:
        if os.path.isfile(item):
            permissionsList = finder(item)
        if color == False:
            if permissions == False:
                if os.path.isfile(item):
                    print(f"FILE: {item}")
                elif os.path.isdir(item):
                    print(f"DIRECTORY: {item}/")
            else:
                if os.path.isfile(item):
                    print(f"FILE: {item} === {''.join(permissionsList)}")
                elif os.path.isdir(item):
                    print(f"DIRECTORY: {item}/")
        else:
            colorlist = []
            readable = False
            writeable = False
            executable = False
            if "+r" in permissionsList:
                readable = True
                colorlist.append(Colors.ForeGround.cyan)
            if "+w" in permissionsList:
                writeable = True
                colorlist.append(Colors.ForeGround.red)
            if "+x" in permissionsList:
                executable = True
                colorlist.append(Colors.ForeGround.lightgreen)      
            if permissions == False:
                if os.path.isfile(item):
                    if len(colorlist) == 3:
                        itemName = ''.join(item.split('.').pop())
                        itemExtension = item.split('.')[-1]
                        firstpart, secondpart = itemName[:len(itemName)//2], itemName[len(itemName)//2:]
                        print(f"FILE: {colorlist[0]}{firstpart}{colorlist[1]}{secondpart}{colorlist[2]}{itemExtension}")
                elif os.path.isdir(item):
                    print(f"DIRECTORY: {item}/")
            else:
                if os.path.isfile(item):
                    if len(colorlist) == 3:
                        itemName = ''.join(item.split('.').pop())
                        itemExtension = item.split('.')[-1]
                        firstpart, secondpart = itemName[:len(itemName)//2], itemName[len(itemName)//2:]
                        print(f"FILE: {colorlist[0]}{firstpart}{colorlist[1]}{secondpart}{colorlist[2]}{itemExtension} === {''.join(permissionsList)}")
                elif os.path.isdir(item):
                    print(f"DIRECTORY: {item}/")
