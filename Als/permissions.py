#!/usr/bin/env python
#permissions.py
"""
File permissions finder module for Als
"""

import os
import sys

def finder(file):
    if os.path.isfile(file) and os.access(file, os.F_OK):
        permissions = []
        if os.access(file, os.R_OK):
            permissions.append("+r")
        if os.access(file, os.W_OK):
            permissions.append("+w")
        if os.access(file, os.X_OK):
            permissions.append("+x")
        return permissions
    else:
        print(f"{file} should be file")
        sys.exit(0)
