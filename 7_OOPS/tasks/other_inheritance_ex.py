#write a python program that define 3 classes :
# details,student and staff, the program demonstarte the use of class inheritance ,
# where students and staff inherit common attributes and methods from the details class
class Details:
    def __init__(self, name, age, id_number):
        self.name = name
        self.age = age
        self.id_number = id_number

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"ID Number: {self.id_number}")


class Student(Details):
    def __init__(self, name, age, id_number, major):
        super().__init__(name, age, id_number)
        self.major = major

    def display_details(self):
        super().display_details()
        print(f"Major: {self.major}")


class Staff(Details):
    def __init__(self, name, age, id_number, position):
        super().__init__(name, age, id_number)
        self.position = position

    def display_details(self):
        super().display_details()
        print(f"Position: {self.position}")


def main():
    print("Enter Student Details:")
    student_name = input("Name: ")
    try:
        student_age = int(input("Age: "))
    except ValueError:
        print("Invalid input for age. Please enter a number.")
        return
    student_id = input("ID Number: ")
    student_major = input("Major: ")
    student = Student(student_name, student_age, student_id, student_major)
    print("\nEnter Staff Details:")
    staff_name = input("Name: ")
    try:
        staff_age = int(input("Age: "))
    except ValueError:
        print("Invalid input for age. Please enter a number.")
        return
    staff_id = input("ID Number: ")
    staff_position = input("Position: ")
    staff = Staff(staff_name, staff_age, staff_id, staff_position)
    print("\nStudent Details:")
    student.display_details()
    print("\nStaff Details:")
    staff.display_details()
main()
