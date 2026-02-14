# Generated from: assignment(EMS).ipynb
# Converted at: 2026-02-13T14:58:12.307Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

# ## Employee Management System (EMS). 


# ### Step 1: Initialize employee data


employee = {
    101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000},
    102: {'name': 'Rohan', 'age': 29, 'department': 'IT', 'salary': 70000},
    103: {'name': 'Monika', 'age': 32, 'department': 'IT', 'salary': 100000},
    104: {'name': 'Moni', 'age': 25, 'department': 'HR', 'salary': 80000},
    105: {'name': 'Nika', 'age': 32, 'department': 'IT', 'salary': 450000}
}

# ### Step 3: Add Employee Function


def add_employee():
    try:
        emp_id = int(input("Enter Employee ID: "))

        if emp_id in employees:
            print("Employee ID already exists. Please enter a unique ID.")
            return

        name = input("Enter Employee Name: ")
        age = int(input("Enter Employee Age: "))
        department = input("Enter Employee department: ")
        salary = float(input("Enter Employee Salary: "))

        employee[emp_id] = {
            'name': name,
            'age': age,
            'department': department,
            'salary': salary
        }

        print("Employee added successfully!")

    except ValueError:
        print("Invaild input. Please enter correct data.")
            
        

# ### Step 4: View All Employees


def view_employees():
    if not employee:
        print("NO employees available.")
        return

    print("\nEmployee Details:")
    print("-" * 60)
    print(f"{'ID':<10}{'Name':<15}{'Age':<10}{'Department':<15}{'Salary':<10}")
    print("-" * 60)

    for emp_id, details in employee.items():
        print(f"{emp_id:<10}{details['name']:<15}{details['age']:<10}{details['department']:<15}{details['salary']:<10}")

    print("-" * 60)

view_employees()

# ### Step 5: Search Employee by ID


def search_employeee():
    try:
        emp_id = int(input("Enter Employee ID to search: "))

        if emp_id in employee:
            emp = employee[emp_id]
            print("\nEmployee Found:")
            print(f"Name          :  {emp['name']}")
            print(f"Name          :  {emp['age']}")
            print(f"Name          :  {emp['department']}")
            print(f"Name          :  {emp['salary']}")
        else:
            print("Employee not found.")

    except ValueError:
        print("Invaild input. Please enter a valid Employee ID.")

# ### Step 2: Define the Menu System


def main_menu():
    while True:
        print("\n--- Employee Management System ---")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice =='3':
            Search_employee()
        elif choice == 4:
            print("Thank you for using this Employee Management System!")
            break       ###Exit
        else:
            print("Invalid choice. Please try again,")

# ## Execution Flow of the Program


# 
# 
# Step 1 - Initialize employee data
# Step 2 - Add Employee Function
# Step 3 - View All Employees
# Step 4 - Search Employee by ID
# Step 5 - Define the Menu System
# Step 7 - Exit the Program (inside menu)
#