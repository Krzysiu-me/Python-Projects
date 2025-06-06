# Lists Example
# Copyright (c) 2025 Krzysiu
# Licensed under the MIT License. See LICENSE file for details.

# Lists are used to store multiple items in one variable.
# Lists can hold any type of data: numbers, strings, even other lists.

fruits = ["apple", "banana", "orange"]
print(f"Fruits: {fruits}")

# Accessing list items by index (starting from 0):
print(f"First fruit: {fruits[0]}")

# Adding items to a list:
fruits.append("kiwi")
print(f"After adding kiwi: {fruits}")

# Removing items:
fruits.remove("banana")
print(f"After removing banana: {fruits}")

# Looping through a list:
for fruit in fruits:
    print(f"I like {fruit}")

# List length:
print(f"Number of fruits: {len(fruits)}")

# Slicing lists (getting a part of a list):
print(f"First two fruits: {fruits[:2]}")
