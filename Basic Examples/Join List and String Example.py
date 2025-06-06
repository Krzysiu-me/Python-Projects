# Join List Into String Example
# Copyright (c) 2025 Krzysiu
# Licensed under the MIT License. See LICENSE file for details.

# Use join() to combine list items into a single string.

words = ["Python", "is", "fun"]
sentence = " ".join(words)   # Joins with spaces between each word
print(f"Sentence: {sentence}")

# You can use any string as the separator:
csv = ",".join(words)        # Joins with commas
print(f"CSV: {csv}")
