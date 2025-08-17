import json
from task import add_task, load_tasks, set_status
from employees import add_employee

def main():
    while True:
        print("\nMAIN MENU")
        print("1. Add employee")
        print("2. Add new task")
        print("3. List tasks")
        print("4. Update task status - BUG TO FIX")
        print("5. Exit")
        print("\nmore options are COMING SOON!")

        choice = input("\nChoose an option: ").strip()
        if choice == "1": 
            add_employee(input("Employee name: "))

        elif choice == "2": add_task()

        elif choice == "3":
            with open('data/tasks.json', 'r', encoding='utf-8') as tasks:

                for task in json.load(tasks).values():
                    print(f"Task ID: {task['id']}, Description: {task['description']}, Status: {task['status']}, Assignee: {task['assignee']}, Priority: {task['priority']}")
                    
        elif choice == "4":
            task_id = input("Enter task ID to update: ")
            tasks = load_tasks()
            task = tasks.get(task_id)
            if task:
                set_status(task)

            else:
                print("Task not found.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
main()