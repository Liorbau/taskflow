from enum import Enum
from dataclasses import dataclass
from datetime import datetime
import json
import os

class Priority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

class Status(Enum):
    WAITING = 1
    WORKING = 2
    COMPLETED = 3

@dataclass
class Task:
    description: str
    id: int
    project: str
    assignee: str
    priority: Priority
    status: Status
    creation_date: datetime
    due_date: datetime

#Getters + Setters
def get_task_status(task):
    return task.Status

def set_status(task):
    if get_task_status(task) == Status.WAITING:
        task.status = Status.WORKING
        print(f"Status of task {task.id} changed to WORKING")
        return 
    
    elif get_task_status(task) == Status.WORKING:
        task.status = Status.COMPLETED

        with open("data/tasks_archive", "a", encoding="utf-8") as archive:
            json.dump(task.__dict__, archive)
            archive.write("\n")

            tasks = load_tasks()
            key = str(task.id)
            if key in tasks:
                del tasks[key]
                with open("data/tasks.json", "w", encoding="utf-8") as tasks_file:
                    json.dump(tasks, tasks_file, indent=4)

        print(f"Task {task.id} completed and archived.")
        return
    
    else:
        raise ValueError("Invalid status change")
        
#==================================================================================================================================================================================================================#
def load_tasks():
    if not os.path.exists('data/tasks.json'):
        return {}
    
    else:
        with open('data/tasks.json', 'r', encoding='utf-8') as tasks_list:
            return json.load(tasks_list)
        
def add_task():
    data = load_tasks()
    
    id = create_id()
    description = input("Please enter a description: ")
    projects = get_existing_projects()
    if projects:
        print("Existing projects:")
        for proj in projects:
            print(f"- {proj}")

    project = input("Enter project name: ")

    employees = load_employees()
    if employees:
        print("Available employees:")
        for eid, info in employees.items():
            print(f"{eid}: {info['name']} ({info['team']})")
    
    else:
        print("No employees found. You must add employees first.")
        return

    assignee_id = input("Enter the ID of the assignee from the list above: ")
    if assignee_id not in employees:
        print("Invalid ID - task not added.")
        return

    assignee = employees[assignee_id]["name"]

    priority_num = input("Define priority (1 = LOW, 2 = MEDIUM, 3 = HIGH): ")
    if priority_num not in ("1", "2", "3"):
        print("Invalid input. Task not added.")
        return

    priority = Priority(int(priority_num)).name 
    
    status = Status(1).name

    creation_date = datetime.now().strftime("%d-%m-%Y")

    due_date_input = input("Enter due date (DD-MM-YYYY): ")
    try:
        due_date = datetime.strptime(due_date_input, "%d-%m-%Y").strftime("%d-%m-%Y")
    except ValueError:
        print("Invalid date format. Task not added.")
        return
    
    new_task = {
        "id": id,
        "description": description,
        "project": project,
        "assignee": assignee,
        "priority": priority,
        "status": status,
        "creation_date": creation_date,
        "due_date": due_date
    }

    
    data[str(id)] = new_task

    with open('data/tasks.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

    print("Task added successfully.")

def create_id():
    with open('data/task_id_counter.json', "r") as counter:
        new_id = json.load(counter)

    with open('data/task_id_counter.json', "w") as counter:
        json.dump(new_id + 1, counter)

def get_existing_projects():
    if not os.path.exists('data/tasks.json'):
        return set()

    with open('data/tasks.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        return {task["project"] for task in data.values()}

def load_employees():
    if not os.path.exists('data/employees.json'):
        return {}
    with open('data/employees.json', 'r', encoding='utf-8') as f:
        return json.load(f)
    
