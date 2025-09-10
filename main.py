import argparse
from cli import create_project, list_projects, add_task, list_tasks, update_task_status, delete_project, delete_task

def show_help():
    """Display the list of available commands."""
    print("""
Available commands:
1. create_project "Project Name" --description "Project Description"
2. list_projects
3. add_task project_id "Task Title" "YYYY-MM-DD" --description "Task Description"
4. list_tasks project_id
5. update_task_status task_id "status" (status: OPEN, IN_PROGRESS, CLOSED)
6. delete_project project_id
7. delete_task task_id
8. exit
    """)

def main():
    # Initialize the loop
    while True:
        # Display the prompt for user input
        print("\nEnter a command (or type 'help' for a list of commands):")
        user_input = input("> ").strip()
        
        # Exit the program if the user types 'exit'
        if user_input.lower() == "exit":
            print("Exiting the application.")
            break
        
        # Process the user command
        if user_input.lower() == "help":
            show_help()
            continue
        
        # Parse the command manually since we have continuous input
        args = user_input.split()
        
        # Handle different commands
        if args[0].lower() == "create_project" and len(args) > 1:
            name = args[1]
            description = args[3] if len(args) > 3 and args[2] == '--description' else ""
            create_project(name, description)
        
        elif args[0].lower() == "list_projects":
            list_projects()
        
        elif args[0].lower() == "add_task" and len(args) > 3:
            project_id = args[1]
            title = args[2]
            deadline = args[3]
            description = args[5] if len(args) > 5 and args[4] == '--description' else ""
            add_task(project_id, title, deadline, description)
        
        elif args[0].lower() == "list_tasks" and len(args) > 1:
            project_id = args[1]
            list_tasks(project_id)
        
        elif args[0].lower() == "update_task_status" and len(args) > 2:
            task_id = args[1]
            status = args[2].upper()  # Ensure status is in uppercase
            update_task_status(task_id, status)
        
        elif args[0].lower() == "delete_project" and len(args) > 1:
            project_id = args[1]
            delete_project(project_id)
        
        elif args[0].lower() == "delete_task" and len(args) > 1:
            task_id = args[1]
            delete_task(task_id)
        
        else:
            print("Unknown command. Type 'help' to see the list of available commands.")

if __name__ == "__main__":
    main()
