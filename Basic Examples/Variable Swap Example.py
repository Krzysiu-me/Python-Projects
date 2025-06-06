# Variable Swapping Example
# Copyright (c) 2025 Krzysiu
# Licensed under the MIT License. See LICENSE file for details.

# Let's swap the values of two variables: a and b

a = 5        # a starts as 5
b = 10       # b starts as 10

print(f"Before swapping: a = {a}, b = {b}")

# This single line swaps their values.
# After this line, a will be 10 and b will be 5
a, b = b, a

print(f"After swapping: a = {a}, b = {b}")

# This works because Python allows multiple assignment on the same line.
