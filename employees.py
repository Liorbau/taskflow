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

def load_employees():
    if not os.path.exists('data/employees.json'):
        return {}
    
    else:
        with open('data/employees.json', 'r', encoding='utf-8') as employees_list:
            return json.load(employees_list)

def add_employee(name: str):
    data = load_employees()
    id = create_id()

    employee = {
                "name": name, 
                "company_id": id,
                "role": Role.WORKER.name
    }

    data[str(id)] = employee
    with open('data/employees.json', 'w', encoding='utf-8') as employees_list:
        json.dump(data, employees_list, indent=4)
    
    print("SUCCESS")

def create_id():
    with open('data/employee_id_counter.json', "r") as counter:
        new_id = json.load(counter)

    with open('data/employee_id_counter.json', "w") as counter:
        json.dump(new_id + 1, counter)

    return new_id

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
        print(print(f"Theres no such id {id}? - FAILED"))
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
    
    else:
        print(f"Who is {id}? - FAILED")
        return False