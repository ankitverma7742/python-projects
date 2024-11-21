import datetime

# File to store task records
tasks_file = "tasks.txt"

# Function to add a new task
def add_task(task_id, description, assigned_to, due_date):
    with open(tasks_file, "a") as file:
        file.write(f"{task_id},{description},{assigned_to},{due_date},Pending\n")
    print(f"Task '{task_id}' added successfully.")

# Function to view all tasks
def view_tasks():
    try:
        with open(tasks_file, "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("No tasks found.")
            else:
                print("Task ID | Description | Assigned To | Due Date  | Status")
                print("-" * 60)
                for task in tasks:
                    task_id, description, assigned_to, due_date, status = task.strip().split(',')
                    print(f"{task_id}      | {description[:10]:<10} | {assigned_to:<10} | {due_date} | {status}")
    except FileNotFoundError:
        print("No tasks found.")

# Function to mark a task as completed
def complete_task(task_id):
    updated_tasks = []
    found = False
    try:
        with open(tasks_file, "r") as file:
            tasks = file.readlines()
            for task in tasks:
                t_id, description, assigned_to, due_date, status = task.strip().split(',')
                if t_id == task_id:
                    updated_tasks.append(f"{t_id},{description},{assigned_to},{due_date},Completed\n")
                    found = True
                else:
                    updated_tasks.append(task)
        if found:
            with open(tasks_file, "w") as file:
                file.writelines(updated_tasks)
            print(f"Task '{task_id}' marked as completed.")
        else:
            print(f"Task '{task_id}' not found.")
    except FileNotFoundError:
        print("No tasks found.")

# Function to view tasks assigned to a specific employee
def view_tasks_by_employee(employee_name):
    try:
        with open(tasks_file, "r") as file:
            tasks = file.readlines()
            found = False
            print(f"Tasks assigned to {employee_name}:")
            print("Task ID | Description | Due Date  | Status")
            print("-" * 50)
            for task in tasks:
                task_id, description, assigned_to, due_date, status = task.strip().split(',')
                if assigned_to == employee_name:
                    print(f"{task_id}      | {description[:10]:<10} | {due_date} | {status}")
                    found = True
            if not found:
                print(f"No tasks found for {employee_name}.")
    except FileNotFoundError:
        print("No tasks found.")

# Main program
def main():
    while True:
        print("\nTask Assignment and Tracking System")
        print("1. Add New Task")
        print("2. View All Tasks")
        print("3. Mark Task as Completed")
        print("4. View Tasks by Employee")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            task_id = input("Enter Task ID: ")
            description = input("Enter Task Description: ")
            assigned_to = input("Assign to Employee: ")
            due_date = input("Enter Due Date (YYYY-MM-DD): ")
            add_task(task_id, description, assigned_to, due_date)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            task_id = input("Enter Task ID to mark as completed: ")
            complete_task(task_id)
        elif choice == "4":
            employee_name = input("Enter Employee Name: ")
            view_tasks_by_employee(employee_name)
        elif choice == "5":
            print("Exiting system.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
