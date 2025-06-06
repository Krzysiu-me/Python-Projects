# Word Counter
# Copyright (c) 2025 Krzysiu
# Licensed under the MIT License. See LICENSE file for details.

# This script counts the number of words, characters, and lines in a given text input by the user.

def main():
    print("--- Word Counter ---")
    print("Paste or type your text below. Enter an empty line to finish:")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    text = "\n".join(lines)
    num_chars = len(text)
    num_words = len(text.split())
    num_lines = len(lines)
    print(f"\nResults:")
    print(f"Characters: {num_chars}")
    print(f"Words: {num_words}")
    print(f"Lines: {num_lines}")
    print("Great work practicing Python!")

if __name__ == "__main__":
    main()
