print("Welcome to your To-Do List!")
print("Let’s help you stay organized.")

tasks = []

try:
    with open("tasks.txt", "r") as file:
        for line in file:
            tasks.append(line.strip())
except FileNotFoundError:
    pass

def view_tasks():
    if not tasks:
        print("No tasks right now.")
    else:
        print("Here are your tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    new_task = input("What do you want to add? ")
    tasks.append(new_task)
    print(f"'{new_task}' added to your list.")

def remove_task():
    view_tasks()
    try:
        number = int(input("Enter the task number to remove: "))
        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            print(f"Removed: {removed}")
        else:
            print("That number isn't on the list.")
    except ValueError:
        print("Please enter a number.")

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

while True:
    print("\nWhat do you want to do now?")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter 1, 2, 3 or 4: ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
        save_tasks()
    elif choice == "3":
        remove_task()
        save_tasks()
    elif choice == "4":
        save_tasks()
        print("All saved. Goodbye!")
        break
    else:
        print("Please enter a valid option (1-4).")
