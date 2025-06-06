# Tip Calculator
# Copyright (c) 2025 Krzysiu
# Licensed under the MIT License. See LICENSE file for details.

def main():
    print("--- Tip Calculator ---")
    try:
        bill = float(input("Enter total bill amount: £"))
        tip_percent = float(input("Enter tip percentage (e.g. 10 for 10%): "))
        people = int(input("How many people to split the bill? "))
        if bill < 0 or tip_percent < 0 or people < 1:
            print("Please enter valid positive values.")
            return
        tip = bill * tip_percent / 100
        total = bill +
