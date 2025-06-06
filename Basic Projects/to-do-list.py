# To-Do List App
# Copyright (c) 2025 Krzysiu
# Licensed under the MIT License. See LICENSE file for details.

# A simple, menu-driven To-Do List App for the terminal. Perfect for beginners.

tasks = []

def show_menu():
    print("\n--- To-Do List App ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Mark Task as Done")
    print("5. Quit")

def view_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        for idx, (task, done) in enumerate(tasks, start=1):
            status = "✔" if done else "✗"
            print(f"{idx}. [{status}] {task}")

def add_task():
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append((task, False))
        print("Task added!")
    else:
        print("Task cannot be empty.")

def remove_task():
    view_tasks()
    if not tasks:
        return
    try:
        idx = int(input("Enter the task number to remove: "))
        if 1 <= idx <= len(tasks):
            removed = tasks.pop(idx - 1)
            print(f"Removed: {removed[0]}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def mark_done():
    view_tasks()
    if not tasks:
        return
    try:
        idx = int(input("Enter the task number to mark as done: "))
        if 1 <= idx <= len(tasks):
            task, _ = tasks[idx - 1]
            tasks[idx - 1] = (task, True)
            print(f"Marked as done: {task}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        show_menu()
        choice = input("Select an option (1-5): ").strip()
        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            mark_done()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-5.")

if __name__ == "__main__":
    main()

