# Simple Timer
# Copyright (c) 2025 Krzysiu
# Licensed under the MIT License. See LICENSE file for details.

import time

def main():
    print("--- Simple Timer ---")
    try:
        minutes = float(input("Enter timer length in minutes: "))
        if minutes <= 0:
            print("Please enter a positive number.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    seconds = int(minutes * 60)
    print(f"Timer started for {minutes} minute(s)...")
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        print(f"Time left: {mins:02d}:{secs:02d}", end="\r")
        time.sleep(1)
        seconds -= 1
    print("\nTime's up!\a")  # '\a' may trigger a beep sound on some systems

if __name__ == "__main__":
    main()
