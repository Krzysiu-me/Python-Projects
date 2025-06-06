# If Statements Example
# Copyright (c) 2025 Krzysiu
# Licensed under the MIT License. See LICENSE file for details.

# If statements let you run code only when a condition is true.

age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")

# Comparing strings:
name = input("What's your name? ")
if name == "Krzysiu":
    print("Hey, that's my name too!")
else:
    print(f"Hello, {name}!")

# Boolean conditions:
is_logged_in = True
if is_logged_in:
    print("Welcome back!")
