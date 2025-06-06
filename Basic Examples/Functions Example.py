# Functions Example
# Copyright (c) 2025 Krzysiu
# Licensed under the MIT License. See LICENSE file for details.

# Functions help you organize your code into blocks that you can reuse.

# This function takes a name and prints a greeting.
def greet(user):
    print(f"Hello, {user}!")

greet("Krzysiu")
greet("World")

# This function adds two numbers and returns the result.
def add(a, b):
    return a + b

sum = add(5, 7)
print(f"5 + 7 = {sum}")

# Functions can have default values:
def say_hello(name="friend"):
    print(f"Hello, {name}!")

say_hello()
say_hello("Alice")
