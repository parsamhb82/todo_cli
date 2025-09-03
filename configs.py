import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Read configs
MAX_TASKS_PER_PROJECT = int(os.getenv("MAX_TASKS_PER_PROJECT", 20))
MAX_PROJECTS = int(os.getenv("MAX_PROJECTS", 10))
MAX_PROJECT_NAME = int(os.getenv("MAX_PROJECT_NAME", 50))
MAX_PROJECT_DESCRIPTION = int(os.getenv("MAX_PROJECT_DESCRIPTION", 100))
MAX_TASK_TITLE = int(os.getenv("MAX_TASK_TITLE", 50))
MAX_TASK_DESCRIPTION = int(os.getenv("MAX_TASK_DESCRIPTION", 200))