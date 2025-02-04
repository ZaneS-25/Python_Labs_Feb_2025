#! /usr/bin/env/ python3
# Author: Zane Salam
# Description: This script will demo how to check with platform the script is running on
"""
    Docstring:
"""

import sys
import os

if sys.platform == "win32":
    home_dir = os.environ["HOMEPATH"]
else:
    home_dir = os.environ["HOME"]


print(home_dir)