#! /usr/bin/env/ python3
# Author: Zane Salam
# Description: This script will simulate a high street bank ATM PIN machine.
"""
    Docstring:
"""

master_pin = "0123"
pin = None
attempts = 0
remaining_attempts = 0
max_attempts = 3

# Loop while PIN is incorrect
while pin != master_pin and attempts != max_attempts:
    pin = input("Enter PIN: ")
    if pin == master_pin:
        print("Valid PIN")
        break
    else:
        attempts += 1
        remaining_attempts = (max_attempts - attempts)

        print("Invalid PIN,", remaining_attempts, "attempts remaining!")
else:
    # Executes ONLY ONCE when loop becomes false
    print("Too many attempts")
    print("The card is being shredded, alerting the authorities!")


print("Done.")