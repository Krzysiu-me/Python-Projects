# Password Generator
# Copyright (c) 2025 Krzysiu
# Licensed under the MIT License. See LICENSE file for details.

import random
import string

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    print("--- Password Generator ---")
    while True:
        try:
            length = input("Enter password length (default 12): ")
            length = int(length) if length else 12
            if length < 4:
                print("Please enter a length of at least 4.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue
        pwd = generate_password(length)
        print(f"Generated password: {pwd}")
        again = input("Generate another? (y/n): ").strip().lower()
        if again != 'y':
            print("Stay secure!")
            break

if __name__ == "__main__":
    main()
