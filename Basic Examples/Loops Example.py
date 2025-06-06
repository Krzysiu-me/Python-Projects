# Loops Example
# Copyright (c) 2025 Krzysiu
# Licensed under the MIT License. See LICENSE file for details.

# Loops let you repeat actions multiple times.

# For loop: repeat for each item in a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")

# For loop with range:
for i in range(1, 6):
    print(f"Number: {i}")

# While loop: repeat as long as a condition is true
count = 0
while count < 3:
    print(f"Counting up: {count}")
    count += 1

# Breaking out of a loop early:
for letter in "hello world":
    if letter == " ":
        break
    print(letter)
