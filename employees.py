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

def add_employee(name: str, team: str):
    data = load_employees()
    id = create_id()

    employee = {
                "name": name, 
                "company_id": id,
                "role": Role.WORKER.name,
                "team": team
    }

    data[str(id)] = employee
    with open('data/employees.json', 'w', encoding='utf-8') as employees_list:
        json.dump(data, employees_list, indent=4)
    
    print("SUCCESS")

def create_id():
    data = load_employees()
    used_ids = {int(id) for id in data.keys()}

    #Lowest available id
    i = 1
    while i in used_ids:
        i += 1

    return i

def fire_employee(id: int):
    data = load_employees()
    key = str(id)
    
    if key in data:
        del data[key]

        with open('data/employees.json', 'w', encoding='utf-8') as employees:
            json.dump(data, employees, indent=4)

        print("SUCCESS")
        return True
    else:
        print("Employee '{employee_name}' (ID: {id}) has been fired - SUCCESS")
        return False
    
def promote_employee(id: int):
    data = load_employees()
    key = str(id)
    
    if key in data:
        current_role = Role[data[key]['role']]
        if current_role == Role.WORKER:
            new_role = Role.TEAM_LEADER
        elif current_role == Role.TEAM_LEADER:
            new_role = Role.DIRECTOR
        elif current_role == Role.DIRECTOR:
            if any(Role[employee['role']] == Role.CEO for employee in data.values()):
                print("There can be only 1 CEO in our company - FAILED promotion")
                return False
            new_role = Role.CEO
        elif current_role == Role.CEO:
            print("Already in the CEO position - FAILED promotion")
            return False
        
        data[key]['role'] = new_role.name

        with open('data/employees.json', 'w', encoding='utf-8') as employees:
            json.dump(data, employees, indent=4)

        print("Promotion succeeded to %s" % new_role.name)
        return True