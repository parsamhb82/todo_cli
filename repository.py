import pickle
import uuid
from typing import List
from datetime import datetime
from entities.models import Project, Task, TaskStatus

class Repository:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.projects: List[Project] = []
        self.tasks: List[Task] = []
        self.load_from_disk()

    def load_from_disk(self):
        """Load data from a pickle file."""
        try:
            with open(self.file_path, "rb") as f:
                data = pickle.load(f)
                self.projects = data.get("projects", [])
                self.tasks = data.get("tasks", [])
        except FileNotFoundError:
            self.projects = []
            self.tasks = []
        except Exception as e:
            print(f"Error loading data: {e}")

    def save_to_disk(self):
        """Save current data to a pickle file."""
        data = {
            "projects": self.projects,
            "tasks": self.tasks
        }
        with open(self.file_path, "wb") as f:
            pickle.dump(data, f)

    # Project Methods
    def save_project(self, project: Project) -> None:
        """Add a project and save to disk."""
        self.projects.append(project)
        self.save_to_disk()

    def get_project(self, project_id: uuid.UUID) -> Project:
        """Retrieve a project by its ID."""
        for project in self.projects:
            if project.__id == project_id:
                return project
        return None

    def get_all_projects(self) -> List[Project]:
        """Retrieve all projects."""
        return self.projects

    def delete_project(self, project_id: uuid.UUID) -> bool:
        """Delete a project by its ID."""
        project = self.get_project(project_id)
        if project:
            self.projects.remove(project)
            self.tasks = [task for task in self.tasks if task.__project_id != project_id]
            self.save_to_disk()
            return True
        return False

    # Task Methods
    def save_task(self, task: Task) -> None:
        """Add a task and save to disk."""
        self.tasks.append(task)
        self.save_to_disk()

    def get_task(self, task_id: uuid.UUID) -> Task:
        """Retrieve a task by its ID."""
        for task in self.tasks:
            if task.__id == task_id:
                return task
        return None

    def get_tasks_for_project(self, project_id: uuid.UUID) -> List[Task]:
        """Retrieve all tasks for a given project."""
        return [task for task in self.tasks if task.__project_id == project_id]

    def update_task_status(self, task_id: uuid.UUID, status: str) -> bool:
        """Update the status of a task."""
        task = self.get_task(task_id)
        if task:
            task.__status = status
            self.save_to_disk()
            return True
        return False

    def delete_task(self, task_id: uuid.UUID) -> bool:
        """Delete a task by its ID."""
        task = self.get_task(task_id)
        if task:
            self.tasks.remove(task)
            self.save_to_disk()
            return True
        return False
