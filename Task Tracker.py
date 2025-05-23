import datetime
import json
import os

# JSON file name
JSON_FILE = "tasks.json"

def load_tasks():
    """Load tasks from JSON file. Create fil if it doesn't exist"""
    if not os.path.exists(JSON_FILE):
        with open(JSON_FILE, 'w', encoding='utf-8') as f: # Add encoding
            json.dump([], f)
        return []
    
    with open(JSON_FILE, 'r', encoding='utf8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []
               
def save_tasks(tasks_list):
    """Save tasks to JSON file."""
    with open(JSON_FILE, 'w', encoding='utf-8') as f: # Add encoding
        json.dump(tasks_list, f, indent=2)

# Load tasks at startup
tasks = load_tasks()

def add_task():
    task_list = input("\ntask-cli add ")
    if not task_list.strip():
        print("-"*50 + "\n")
        print("Task cannot be empty. Please enter a valid task.")
        return
    tasks.append ({"task": task_list, "completed": False})
    save_tasks(tasks)
    print(f"task-cli '{task_list}' added to the list -\n")
    x = datetime.datetime.now()
    print(x.strftime("%c"))

def complete_task():
    list_tasks()
    user_input = input("Task to mark as completed: ")

    try:
        task_to_complete = int(user_input)
        i = task_to_complete - 1

        if 0 <= i < len(tasks):
            tasks[i]["completed"] = True
            save_tasks(tasks) # Save to file
            print(f"Task {task_to_complete} marked as completed! -\n")
        else:
            print("\n" + "-"*50)
            print(f"Invalid task number: '{task_to_complete}' please enter a valid integer between 1 and {len(tasks)}")
            print("-"*50 + "\n")

    except ValueError:
        print("\n" + "*"*50)
        print(f"ERROR: '{user_input}' is not a valid number. Please enter a valid integer.\n")
        print("*"*50 + "\n")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}\n")

def update_task():
    task = input("\ntask-cli update ")
    try:
        i = int(task) - 1
        new_task = input('task-cli ')
        if 0 <= i < len(tasks):
            tasks[i]["task"] = new_task
            save_tasks(tasks)
            print(f"task-cli '{task}' edited -\n")
        else:
            print("\n" + "-"*50)
            print(f"Invalid task number: '{task}' is out of range please enter a valid integer between 1 and {len(tasks)}")
            print("-"*50 + "\n")
    except ValueError:
        print("\n" + "*"*50)
        print(f"ERROR: '{task}' is not a valid number. Please enter a valid task number.")
        print("*"*50 + "\n")
    except Exception as e:
        print(f"An error occurred: {e}")

def list_tasks():
    if not tasks:
        print("There are no tasks currently to complete")
        return
    
    print("Current Tasks: ")
    print("task-cli list:")
    for index, task in enumerate(tasks):
        status = "✓" if task["completed"] else "✗"
        print(f"{index + 1}. [{status}] {task['task']}")

def delete_task():
    list_tasks()
    user_input = input("Enter number to delete: ")
    task_to_delete = None
    
    try:
        task_to_delete = int(user_input)
    except ValueError:
        print("\n" + "*"*50)
        print(f"ERROR: '{task_to_delete}' is not a valid number. Please enter a valid integer.\n")
        print("*"*50 + "\n")
        return
    except Exception as e:
        print(f"An error occurred: {e}\n")
        
    if 0 <= task_to_delete - 1 < len(tasks):
        deleted_task = tasks.pop(task_to_delete - 1)
        save_tasks(tasks)
        print(f"task-cli {task_to_delete} ('{deleted_task['task']}') has been removed -\n")
        x = datetime.datetime.now()
        print(x.strftime("%c"))
    else:
        print("\n" + "-"*50)
        print(f"Invalid task number: '{task_to_delete}' is out of range. Please enter a valid number between 1 and {len(tasks)}.")
        print("-"*50 + "\n")
        
if __name__ == "__main__":
    while True:
        print("\n")
        print("Please select one of the following options")
        print("_"*50 + "\n")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Quit")
        print("5. Update")
        print("6. Complete a task")

        choice = input("\nEnter choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            delete_task()
        elif choice == "3":
            list_tasks()
        elif choice == "4":
            break
        elif choice == "5":
            update_task()
        elif choice == "6":
            complete_task()
        else:
            print(f"Please enter a valid option between 1-6, not '{choice}'")
