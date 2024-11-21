import datetime

# File to store attendance records
attendance_file = "attendance.txt"

# Function to mark attendance for an employee
def mark_attendance(employee_id):
    date = datetime.date.today()
    time = datetime.datetime.now().time()
    with open(attendance_file, "a") as file:
        file.write(f"{employee_id},{date},{time}\n")
    print(f"Attendance marked for Employee ID {employee_id} on {date} at {time}")

# Function to view all attendance records
def view_attendance():
    try:
        with open(attendance_file, "r") as file:
            records = file.readlines()
            if not records:
                print("No attendance records found.")
            else:
                print("Employee ID | Date       | Time")
                print("-" * 30)
                for record in records:
                    employee_id, date, time = record.strip().split(',')
                    print(f"{employee_id}         | {date} | {time}")
    except FileNotFoundError:
        print("No attendance records found.")

# Function to check if a specific employee was present on a specific date
def check_attendance(employee_id, date):
    try:
        with open(attendance_file, "r") as file:
            records = file.readlines()
            for record in records:
                emp_id, record_date, _ = record.strip().split(',')
                if emp_id == employee_id and record_date == date:
                    print(f"Employee ID {employee_id} was present on {date}.")
                    return
            print(f"Employee ID {employee_id} was not present on {date}.")
    except FileNotFoundError:
        print("No attendance records found.")

# Main program
def main():
    while True:
        print("\nEmployee Attendance System")
        print("1. Mark Attendance")
        print("2. View Attendance Records")
        print("3. Check Attendance for a Specific Date")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            employee_id = input("Enter Employee ID: ")
            mark_attendance(employee_id)
        elif choice == "2":
            view_attendance()
        elif choice == "3":
            employee_id = input("Enter Employee ID: ")
            date = input("Enter date (YYYY-MM-DD): ")
            check_attendance(employee_id, date)
        elif choice == "4":
            print("Exiting system.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
