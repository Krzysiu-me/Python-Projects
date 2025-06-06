
# Number Guessing Game
# Copyright (c) 2025 Krzysiu
# Licensed under the MIT License. See LICENSE file for details.

import random

def main():
    print("--- Number Guessing Game ---")
    print("I'm thinking of a number between 1 and 100.")
    number = random.randint(1, 100)
    attempts = 0
    
    while True:
        guess = input("Take a guess: ")
        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid integer.")
            continue
        attempts += 1
        if guess < number:
            print("Too low. Try again.")
        elif guess > number:
            print("Too high. Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} tries.")
            break

if __name__ == "__main__":
    main()
