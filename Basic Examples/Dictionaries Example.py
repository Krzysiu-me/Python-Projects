# Dictionaries Example
# Copyright (c) 2025 Krzysiu
# Licensed under the MIT License. See LICENSE file for details.

# Dictionaries store key-value pairs, like a real dictionary (word: definition)

person = {
    "name": "Krzysiu",
    "age": 20,
    "is_student": True,
    "height": 1.83
}

# Accessing values by key:
print(f"Name: {person['name']}")
print(f"Age: {person['age']}")

# Adding or updating values:
person["city"] = "London"
person["age"] = 21
print(f"Updated person: {person}")

# Looping through dictionary items:
for key, value in person.items():
    print(f"{key}: {value}")

# Checking if a key exists:
if "height" in person:
    print(f"Height: {person['height']} meters")
