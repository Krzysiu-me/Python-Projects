
# Simple Calculator
# Copyright (c) 2025 Krzysiu
# Licensed under the MIT License. See LICENSE file for details.

# This is a simple command-line calculator that supports addition, subtraction, multiplication, and division.

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b

def main():
    print("--- Simple Calculator ---")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    while True:
        choice = input("Enter choice (1/2/3/4) or 'q' to quit: ").strip()
        if choice.lower() == 'q':
            print("Goodbye!")
            break
        if choice not in ['1', '2', '3', '4']:
            print("Invalid input. Try again.")
            continue
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Please enter valid numbers.")
            continue
        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            result = divide(num1, num2)
        print(f"Result: {result}")

if __name__ == "__main__":
    main()
