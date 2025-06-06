# Simple Unit Converter
# Copyright (c) 2025 Krzysiu
# Licensed under the MIT License. See LICENSE file for details.

# Converts between centimeters/inches and kilograms/pounds.

def main():
    print("--- Simple Unit Converter ---")
    while True:
        print("1. Centimeters to Inches")
        print("2. Inches to Centimeters")
        print("3. Kilograms to Pounds")
        print("4. Pounds to Kilograms")
        print("5. Quit")
        choice = input("Choose an option (1-5): ").strip()
        try:
            if choice == '1':
                cm = float(input("Centimeters: "))
                print(f"{cm} cm = {cm / 2.54:.2f} in")
            elif choice == '2':
                inch = float(input("Inches: "))
                print(f"{inch} in = {inch * 2.54:.2f} cm")
            elif choice == '3':
                kg = float(input("Kilograms: "))
                print(f"{kg} kg = {kg * 2.20462:.2f} lbs")
            elif choice == '4':
                lbs = float(input("Pounds: "))
                print(f"{lbs} lbs = {lbs / 2.20462:.2f} kg")
            elif choice == '5':
                print("Goodbye!")
                break
            else:
                print("Please choose a valid option (1-5).")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
