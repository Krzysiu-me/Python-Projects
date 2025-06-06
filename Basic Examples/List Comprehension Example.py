# List Comprehension Example
# Copyright (c) 2025 Krzysiu
# Licensed under the MIT License. See LICENSE file for details.

# List comprehensions are a short way to make new lists by transforming each item.

numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]  # Squares every number in the list
print(f"Original numbers: {numbers}")
print(f"Squares: {squares}")

# You can also filter items:
evens = [x for x in numbers if x % 2 == 0]
print(f"Even numbers: {evens}")
