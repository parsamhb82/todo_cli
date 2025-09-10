import argparse
from entities.models import Project, Task, TaskStatus
from datetime import datetime
from repository import Repository
import uuid

repo = Repository(file_path="data.pkl")

def create_project(name: str, description: str = ""):
    """Create a new project."""
    try:
        project = Project(name=name, description=description)
        repo.save_project(project)
        print(f"Project '{name}' created successfully!")
    except ValueError as e:
        print(f"Error: {e}")

def list_projects():
    """List all projects."""
    projects = repo.get_all_projects()
    if projects:
        for project in projects:
            print(f"Project ID: {project.__id}, Name: {project.__name}, Description: {project.__description}")
    else:
        print("No projects found.")

def add_task(project_id: str, title: str, deadline: str, description: str = ""):
    """Add a task to a project."""
    try:
        project_id_uuid = uuid.UUID(project_id)
        deadline_date = datetime.strptime(deadline, "%Y-%m-%d")
        task = Task(title=title, project_id=project_id_uuid, deadline=deadline_date, description=description)
        repo.save_task(task)
        print(f"Task '{title}' added to project ID: {project_id}.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")

def list_tasks(project_id: str):
    """List all tasks for a specific project."""
    try:
        project_id_uuid = uuid.UUID(project_id)
        tasks = repo.get_tasks_for_project(project_id_uuid)
        if tasks:
            for task in tasks:
                print(f"Task ID: {task.__id}, Title: {task.__title}, Status: {task.__status}, Deadline: {task.__deadline}")
        else:
            print(f"No tasks found for project ID: {project_id}")
    except ValueError as e:
        print(f"Error: {e}")

def update_task_status(task_id: str, status: str):
    """Update the status of a task."""
    try:
        task_id_uuid = uuid.UUID(task_id)
        if status not in [TaskStatus.OPEN, TaskStatus.IN_PROGRESS, TaskStatus.CLOSED]:
            print(f"Invalid status. Valid statuses are: {TaskStatus.OPEN}, {TaskStatus.IN_PROGRESS}, {TaskStatus.CLOSED}")
            return
        if repo.update_task_status(task_id_uuid, status):
            print(f"Task {task_id} status updated to {status}.")
        else:
            print(f"Task {task_id} not found.")
    except ValueError as e:
        print(f"Error: {e}")

def delete_project(project_id: str):
    """Delete a project and its tasks."""
    try:
        project_id_uuid = uuid.UUID(project_id)
        if repo.delete_project(project_id_uuid):
            print(f"Project with ID {project_id} deleted successfully.")
        else:
            print(f"Project with ID {project_id} not found.")
    except ValueError as e:
        print(f"Error: {e}")

def delete_task(task_id: str):
    """Delete a task."""
    try:
        task_id_uuid = uuid.UUID(task_id)
        if repo.delete_task(task_id_uuid):
            print(f"Task with ID {task_id} deleted successfully.")
        else:
            print(f"Task with ID {task_id} not found.")
    except ValueError as e:
        print(f"Error: {e}")
