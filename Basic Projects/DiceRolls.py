
# Dice Rolling Simulator
# Copyright (c) 2025 Krzysiu
# Licensed under the MIT License. See LICENSE file for details.

import random

def roll_dice(sides=6):
    """Roll a dice with the given number of sides (default is 6)."""
    return random.randint(1, sides)

def main():
    print("--- Dice Roller ---")
    while True:
        sides = input("Enter number of sides for the dice (default 6): ")
        if not sides:
            sides = 6
        else:
            try:
                sides = int(sides)
                if sides < 2:
                    print("A dice must have at least 2 sides. Try again.")
                    continue
            except ValueError:
                print("Please enter a valid number.")
                continue
        roll = roll_dice(sides)
        print(f"You rolled a {roll}!")
        again = input("Roll again? (y/n): ").strip().lower()
        if again != 'y':
            print("Thanks for rolling!")
            break

if __name__ == "__main__":
    main()
