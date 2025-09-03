import uuid
from datetime import datetime
from configs import MAX_PROJECT_DESCRIPTION, MAX_PROJECT_NAME, MAX_TASK_TITLE, MAX_TASK_DESCRIPTION
from typing import List

class Project:
    def __init__(self, name: str, description: str = "") -> None:
        if not name or name.strip() == "":
            raise ValueError("Project name is required.")
        if len(name) > MAX_PROJECT_NAME:
            raise ValueError(f"Project name must be {MAX_PROJECT_NAME} characters or fewer.")
        if len(description) > MAX_PROJECT_DESCRIPTION:
            raise ValueError(f"Project description must be {MAX_PROJECT_DESCRIPTION} characters or fewer.")

        self.__id: uuid.UUID = uuid.uuid4()  # unique project identifier
        self.__name: str = name
        self.__description: str = description
        self.__tasks: List["Task"] = []
        self.__created_at: datetime = datetime.now()


class TaskStatus:
    OPEN = "OPEN"
    IN_PROGRESS = "IN_PROGRESS"
    CLOSED = "CLOSED"


class Task:
    def __init__(self, title: str, project_id: uuid.UUID, deadline: datetime, description: str = "") -> None:
        if not title or title.strip() == "":
            raise ValueError("Task title is required.")
        if len(title) > MAX_TASK_TITLE:
            raise ValueError(f"Task title must be {MAX_TASK_TITLE} characters or fewer.")
        if len(description) > MAX_TASK_DESCRIPTION:
            raise ValueError(f"Task description must be {MAX_TASK_DESCRIPTION} characters or fewer.")

        self.__id: uuid.UUID = uuid.uuid4()
        self.__project_id: uuid.UUID = project_id
        self.__title: str = title
        self.__status: str = TaskStatus.OPEN
        self.__created_at: datetime = datetime.now()
        self.__deadline: datetime = deadline
        self.__description: str = description
