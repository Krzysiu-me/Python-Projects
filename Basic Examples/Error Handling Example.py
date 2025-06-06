# Error Handling Example
# Copyright (c) 2025 Krzysiu
# Licensed under the MIT License. See LICENSE file for details.

# try...except lets you handle errors gracefully.

try:
    # Try to convert user input to an integer
    num = int(input("Enter a number: "))
    print(f"You entered: {num}")
except ValueError:
    # If the conversion fails, this code runs
    print("That was not a valid number. Please enter an integer.")

# This stops your program from crashing if the user types text instead of a number.
