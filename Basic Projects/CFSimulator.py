# Coin Flip Simulator
# Copyright (c) 2025 Krzysiu
# Licensed under the MIT License. See LICENSE file for details.

import random

def flip_coin():
    return random.choice(["Heads", "Tails"])

def main():
    print("--- Coin Flip Simulator ---")
    while True:
        input("Press ENTER to flip the coin (or type 'q' to quit): ")
        result = flip_coin()
        print(f"Result: {result}")
        again = input("Flip again? (y/n): ").strip().lower()
        if again != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
