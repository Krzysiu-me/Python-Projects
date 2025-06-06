# Days Until Birthday
# Copyright (c) 2025 Krzysiu
# Licensed under the MIT License. See LICENSE file for details.

from datetime import datetime, date

def main():
    print("--- Days Until Birthday ---")
    today = date.today()
    try:
        bday_str = input("Enter your birthday (DD-MM): ").strip()
        day, month = map(int, bday_str.split('-'))
        this_year_bday = date(today.year, month, day)
        if this_year_bday < today:
            next_bday = date(today.year + 1, month, day)
        else:
            next_bday = this_year_bday
        delta = (next_bday - today).days
        print(f"Your birthday is in {delta} day(s)!")
    except Exception:
        print("Invalid date format. Please use DD-MM.")

if __name__ == "__main__":
    main()
