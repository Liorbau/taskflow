from enum import Enum
import json
import os

class Role(Enum):
    WORKER = 1
    TEAM_LEADER = 2
    DIRECTOR = 3
    CEO = 4

#class Employee


def load_employees():
    if not os.path.exists('data/employees.json'):
        return {}
    
    else:
        with open('data/employees.json', 'r', encoding='utf-8') as employees_list:
            return json.load(employees_list)

#def add_assignee(name: str, )