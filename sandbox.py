# sandbox.py

def display_menu():
    print("\n--- To do list ---")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Edit task")
    print("5. Exit")

def show_tasks(tasks):
    if not tasks:
        print("Tasks list is empty")
    else:
        print("\nYour tasks")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def add_task(tasks):
    task = input("Input your task: ")
    tasks.append(task)
    print(f"Task '{task}' is added")

def delete_task(tasks):
    show_tasks(tasks)
    if tasks:
        try:
            idx = int(input("Choose number for delete: "))
            if 1 <= len(tasks):
                removed_task = tasks.pop(idx - 1)
                print(f"Tasks '{removed_task}' deleted.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please, choose correct number")

def edit_task(tasks):
    show_tasks(tasks)
    if tasks:
        try:
            idx = int(input("Choose task number to edit: "))
            if 1 <= idx <= len(tasks):
                new_task = input("Write new task description: ")
                old_task - tasks[idk - 1]
                tasks[idk - 1] = new_task
                print(f"Task '{old_task}' has been changed to '{new_task}'.")
            else:
                print("Invalid task number")
        except ValueError:
            print("Please, choose correct number")

def main():
    tasks = []
    while True:
        display_menu()
        choise = input("Choose option: ")
        if choise == "1":
            show_tasks(tasks)
        elif choise == "2":
            add_task(tasks)
        elif choise == "3":
            delete_task(tasks)
        elif choise == "4":
            edit_task(tasks)
        elif choise == "5":
            print("Exit")
            break
        else:
            print("Wrong choise. Try again.")

if __name__ == "__main__":
    main()