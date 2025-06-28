import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f)

# Load tasks at start
try:
    task = load_tasks()
except Exception:
    task = []

while True:
    print("\n--- To_Do List ---")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Delete a task")
    print("4. Mark task as completed")
    print("5. Edit a task")
    print("6. Quit")
    
    choice = input("choose an option(1-6): ")
    
    if choice == "1":
        new_task = input("Enter your task: ")
        task.append({'desc': new_task, 'done': False})
        save_tasks(task)
        print("Task added!")
    
    elif choice == "2":
        print("\n Your task:")
        if not task:
            print("No tasks yet.")
        else:
            for i, t in enumerate(task, 1):
                status = "✓" if t['done'] else " "
                print(f"{i}. [{status}] {t['desc']}")
    
    elif choice == "3":
        if not task:
            print("No tasks to delete.")
        else:
            for i, t in enumerate(task, 1):
                status = "✓" if t['done'] else " "
                print(f"{i}. [{status}] {t['desc']}")
            try:
                del_num = int(input("Enter the number of the task to delete: "))
                if 1 <= del_num <= len(task):
                    removed = task.pop(del_num - 1)
                    save_tasks(task)
                    print(f'Task "{removed["desc"]}" deleted!')
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
    
    elif choice == "4":
        if not task:
            print("No tasks to mark as completed.")
        else:
            for i, t in enumerate(task, 1):
                status = "✓" if t['done'] else " "
                print(f"{i}. [{status}] {t['desc']}")
            try:
                comp_num = int(input("Enter the number of the task to mark as completed: "))
                if 1 <= comp_num <= len(task):
                    task[comp_num - 1]['done'] = True
                    save_tasks(task)
                    print(f'Task "{task[comp_num - 1]["desc"]}" marked as completed!')
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
    
    elif choice == "5":
        if not task:
            print("No tasks to edit.")
        else:
            for i, t in enumerate(task, 1):
                status = "✓" if t['done'] else " "
                print(f"{i}. [{status}] {t['desc']}")
            try:
                edit_num = int(input("Enter the number of the task to edit: "))
                if 1 <= edit_num <= len(task):
                    new_desc = input("Enter the new description: ")
                    task[edit_num - 1]['desc'] = new_desc
                    save_tasks(task)
                    print("Task updated!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
    
    elif choice == "6":
        print("Goodbye, JAmes! stay productive")
        break
    
    else:
        print("Invalid choice. please try again")

