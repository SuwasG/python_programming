import os

# Define the file to store the tasks
TODO_FILE = 'todo_list.txt'

def load_tasks():
    """Load tasks from the file."""
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            tasks = file.read().splitlines()
    else:
        tasks = []
    return tasks

def save_tasks(tasks):
    """Save tasks to the file."""
    with open(TODO_FILE, 'w') as file:
        file.write('\n'.join(tasks))

def display_tasks(tasks):
    """Display the current list of tasks."""
    if not tasks:
        print("Your to-do list is empty!")
    else:
        print("\nYour to-do list:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks):
    """Add a new task to the list."""
    task = input("Enter the new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task}' added to the list.")

def remove_task(tasks):
    """Remove a task from the list."""
    display_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Task '{removed_task}' removed from the list.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Menu:")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Remove a task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option, please choose again.")

if __name__ == "__main__":
    main()
