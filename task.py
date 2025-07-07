from enum import Enum
from dataclasses import dataclass
from datetime import datetime

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