#! /usr/bin/env/ python3
# Author: Zane Salam
# Description: This script will demo how to repeat a block of commands
# a specific # of times using a COUNTER loop.
"""
    Docstring:
"""
count = 0           # Initialize counter
while count < 10:   # Test counter
    print(count)    # Print counter
    count += 1      # Increment counter


#Alternativly, we could use a FOR loop plus the built-in RANGE function.
# range(start, stop, step) function.
for num in range(0, 10, 1):
    print(num)


# range(start, stop, step=1) function.
for num in range(0, 10):
    print(num)


# range(start=0, stop, step=1) function.
for num in range(10):
    print(num)

