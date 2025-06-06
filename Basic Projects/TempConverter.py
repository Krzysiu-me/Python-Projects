# Temperature Converter
# Copyright (c) 2025 Krzysiu
# Licensed under the MIT License. See LICENSE file for details.

# This program converts temperatures between Celsius and Fahrenheit.

def c_to_f(c):
    return c * 9 / 5 + 32

def f_to_c(f):
    return (f - 32) * 5 / 9

def main():
    print("--- Temperature Converter ---")
    while True:
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Quit")
        choice = input("Select an option (1-3): ").strip()
        if choice == '1':
            try:
                c = float(input("Enter temperature in Celsius: "))
                print(f"{c}°C = {c_to_f(c):.2f}°F")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '2':
            try:
                f = float(input("Enter temperature in Fahrenheit: "))
                print(f"{f}°F = {f_to_c(f):.2f}°C")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
