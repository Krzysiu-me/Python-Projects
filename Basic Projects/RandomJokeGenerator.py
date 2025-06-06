# Random Joke Generator
# Copyright (c) 2025 Krzysiu
# Licensed under the MIT License. See LICENSE file for details.

import random

JOKES = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the computer show up at work late? It had a hard drive!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why did the bicycle fall over? Because it was two-tired!",
    "What do you call fake spaghetti? An impasta!",
    "Why can’t you hear a pterodactyl go to the bathroom? Because the 'P' is silent!"
]

def tell_joke():
    return random.choice(JOKES)

def main():
    print("--- Random Joke Generator ---")
    while True:
        input("Press ENTER to hear a joke (or type 'q' to quit): ")
        print(tell_joke())
        again = input("Want another joke? (y/n): ").strip().lower()
        if again != 'y':
            print("Goodbye! Keep smiling!")
            break

if __name__ == "__main__":
    main()
