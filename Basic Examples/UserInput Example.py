# User Input Example
# Copyright (c) 2025 Krzysiu
# Licensed under the MIT License. See LICENSE file for details.

# You can ask the user for input using the input() function.

name = input("What's your name? ")
print(f"Hello, {name}!")

# Getting numbers from the user (always convert input to int or float):
age = int(input("How old are you? "))
print(f"You are {age} years old.")

# Simple quiz using user input:
answer = input("What is 2 + 2? ")
if answer == "4":
    print("Correct!")
else:
    print("Oops, try again.")
