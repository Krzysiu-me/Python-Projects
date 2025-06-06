# Leap Year Checker
# Copyright (c) 2025 Krzysiu
# Licensed under the MIT License. See LICENSE file for details.

def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def main():
    print("--- Leap Year Checker ---")
    while True:
        entry = input("Enter a year (or 'q' to quit): ").strip()
        if entry.lower() == 'q':
            print("Goodbye!")
            break
        try:
            year = int(entry)
            if is_leap(year):
                print(f"{year} is a leap year.")
            else:
                print(f"{year} is not a leap year.")
        except ValueError:
            print("Please enter a valid year.")

if __name__ == "__main__":
    main()
