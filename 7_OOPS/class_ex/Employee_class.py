#write a python class Employee with attribute like,
#employee_id,employee_name,employee_salary,employee_department,leave_total
#and methods like
#read_details,calculate_employee_salary,employee_assigned_department, print_employee_details
#calculate salary = totalsalary-leave

class Employee:
    def read_details(self):
        self.employee_id = input("Enter employee ID: ")
        self.employee_name = input("Enter employee name: ")
        self.employee_salary = float(input("Enter employee salary: "))
        self.employee_department = input("Enter employee department: ")
        self.leave_total = float(input("Enter total leave: "))

    def display_details(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"Employee Name: {self.employee_name}")
        print(f"Employee Actual Salary: {self.employee_salary}")
        print(f"Employee Department: {self.employee_department}")
        print(f"Leave Total: {self.leave_total}")

    def calculate_employee_salary(self):
        salary_after_leaves = self.employee_salary - (self.leave_total * 100)
        return salary_after_leaves
    def print_employee_details(self):
        self.read_details()
        print("Employee Details")
        print("-" * 36)
        self.display_details()
        print(f"Salary after leave deduction: {self.calculate_employee_salary()}")

emp = Employee()
emp.print_employee_details()
