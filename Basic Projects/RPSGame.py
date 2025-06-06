# Rock Paper Scissors Game
# Copyright (c) 2025 Krzysiu
# Licensed under the MIT License. See LICENSE file for details.

import random

def main():
    print("--- Rock Paper Scissors ---")
    moves = ["rock", "paper", "scissors"]
    while True:
        user_move = input("Enter your move (rock/paper/scissors or q to quit): ").strip().lower()
        if user_move == 'q':
            print("Thanks for playing!")
            break
        if user_move not in moves:
            print("Invalid move. Try again.")
            continue
        comp_move = random.choice(moves)
        print(f"Computer chose: {comp_move}")
        if user_move == comp_move:
            print("It's a tie!")
        elif (
            (user_move == "rock" and comp_move == "scissors") or
            (user_move == "paper" and comp_move == "rock") or
            (user_move == "scissors" and comp_move == "paper")
        ):
            print("You win!")
        else:
            print("You lose!")

if __name__ == "__main__":
    main()
