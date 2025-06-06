# Simple Quiz Game
# Copyright (c) 2025 Krzysiu
# Licensed under the MIT License. See LICENSE file for details.

# This is a simple multiple-choice quiz game for learning/practice.

QUESTIONS = [
    {
        'question': "What is the capital of France?",
        'choices': ['A) Berlin', 'B) Paris', 'C) Rome', 'D) Madrid'],
        'answer': 'B'
    },
    {
        'question': "Which language is primarily used for web development?",
        'choices': ['A) Python', 'B) Java', 'C) JavaScript', 'D) C++'],
        'answer': 'C'
    },
    {
        'question': "What does RAM stand for?",
        'choices': ['A) Read Access Memory', 'B) Random Access Memory', 'C) Run Access Memory', 'D) Readily Available Memory'],
        'answer': 'B'
    },
    {
        'question': "Which of these is a Python data type?",
        'choices': ['A) list', 'B) queue', 'C) node', 'D) heap'],
        'answer': 'A'
    },
]

def main():
    print("--- Simple Quiz Game ---")
    score = 0
    for q in QUESTIONS:
        print("\n" + q['question'])
        for choice in q['choices']:
            print(choice)
        user_ans = input("Your answer (A/B/C/D): ").strip().upper()
        if user_ans == q['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct answer is {q['answer']}.")
    print(f"\nQuiz Over! Your score: {score}/{len(QUESTIONS)}")
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
