import uuid
from datetime import datetime
from configs import MAX_PROJECT_DESCRIPTION, MAX_PROJECT_NAME, MAX_TASK_TITLE, MAX_TASK_DESCRIPTION


class Project:
    def __init__(self, name, description=""):

        if not name or name.strip() == "":
            raise ValueError("Project name is required.")
        if len(name) > MAX_PROJECT_NAME:
            raise ValueError(f"Project name must be {MAX_PROJECT_NAME} characters or fewer.")
        if len(description) > MAX_PROJECT_DESCRIPTION:
            raise ValueError(f"Project description must be {MAX_PROJECT_DESCRIPTION} characters or fewer.")

        self.__id = uuid.uuid4() ## can be used to uniquely identify the project 
        self.__name = name
        self.__description = description
        self.__tasks = []
        self.__created_at = datetime.now()



class Task:
    def __init__(self, title, project_id, deadline, description=""):

        if not title or title.strip() == "":
            raise ValueError("Task title is required.")
        if len(title) > MAX_TASK_TITLE:
            raise ValueError(f"Task title must be {MAX_TASK_TITLE} characters or fewer.")
        if len(description) > MAX_TASK_DESCRIPTION:
            raise ValueError(f"Task description must be {MAX_TASK_DESCRIPTION} characters or fewer.")

        self.__id = uuid.uuid4()
        self.__project_id = project_id
        self.__title = title
        self.__status = "TODO"
        self.__created_at = datetime.now()
        self.__deadline = deadline
        self.__description = description

    def mark_done(self):
        self.done = True

    def mark_pending(self):
        self.done = False

    def __repr__(self):
        return f"Task(title={self.title!r}, done={self.done})"