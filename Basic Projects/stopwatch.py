
# Simple Stopwatch
# Copyright (c) 2025 Krzysiu
# Licensed under the MIT License. See LICENSE file for details.

import time

def main():
    print("--- Simple Stopwatch ---")
    print("Press ENTER to start the stopwatch.")
    input()
    start = time.time()
    print("Stopwatch started. Press ENTER to stop.")
    input()
    end = time.time()
    elapsed = end - start
    mins, secs = divmod(elapsed, 60)
    print(f"Elapsed Time: {int(mins):02d}:{secs:05.2f} (mm:ss.ss)")
    print("Good job!")

if __name__ == "__main__":
    main()
