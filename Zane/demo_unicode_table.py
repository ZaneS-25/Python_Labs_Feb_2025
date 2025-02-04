#! /usr/bin/env/ python3
# Author: Zane Salam
# Description: This script will demo how to display the entire unicdoe char set
"""
    Docstring:
"""

# ITERATE through all the chars in the Unicode table
# using an ITERATOR for loop (0->65535)
for pos in range(0,65536):
    try:
        print(chr(pos), end=" ")
        if pos % 16 == 0:
            print()
    except UnicodeError:
        print(" ")