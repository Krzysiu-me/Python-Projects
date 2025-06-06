# Slicing Example
# Copyright (c) 2025 Krzysiu
# Licensed under the MIT License. See LICENSE file for details.

# Slicing lets you get a part of a list or string by specifying the start and end index.

my_list = [1, 2, 3, 4, 5]
print(f"Full list: {my_list}")
print(f"Items from index 1 up to (not including) 4: {my_list[1:4]}")  # Outputs [2, 3, 4]

my_string = "abcdef"
print(f"Characters from index 2 up to (not including) 5: {my_string[2:5]}")  # Outputs "cde"

# Remember: Slicing does not include the character at the end index.
