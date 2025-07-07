from enum import Enum
from dataclasses import dataclass
import json
import os

class Role(Enum):
    WORKER = 1
    TEAM_LEADER = 2
    DIRECTOR = 3
    CEO = 4

@dataclass
class Employee:
    name: str
    company_id: int
    role: Role
    team: str
    # Add later tasks by employee

def load_employees():
    if not os.path.exists('data/employees.json'):
        return {}
    
    else:
        with open('data/employees.json', 'r', encoding='utf-8') as employees_list:
            return json.load(employees_list)

def add_employees(name: str, team: str):
    data = load_employees()
    id = create_id()

    employee = {
                "name": name, 
                "company_id": id,
                "role": Role.WORKER,
                "team": team
    }

    data[str(id)] = employee
    with open('data/employees.json', 'w', encoding='utf-8') as employees_list:
        json.dump(data, employees_list, indent=4)

def create_id():
    data = load_employees()
    used_ids = {int(id) for id in data.keys()}

    #Lowest available id
    i = 1
    while i in used_ids:
        i += 1

    return i