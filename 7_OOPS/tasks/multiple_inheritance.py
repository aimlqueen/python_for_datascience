#write a python program to
# demonstrate the concept of multiple inheritance
# by creating a child inherit the two parent  classess :
# personal_info and academic_info,
# the program collects personal and acadmic
# information from the user and then display the student details in student class

class PersonalInfo:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class AcademicInfo:
    def __init__(self, student_id, major):
        self.student_id = student_id
        self.major = major

class Student(PersonalInfo, AcademicInfo):
    def __init__(self, name, age, student_id, major):
        PersonalInfo.__init__(self, name, age)
        AcademicInfo.__init__(self, student_id, major)

    def display_details(self):
        print("\nStudent Details:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Student ID: {self.student_id}")
        print(f"Major: {self.major}")

def main():
    print("Enter Student Information:")
    name = input("Enter student's name: ")
    try:
        age = int(input("Enter student's age: "))
    except ValueError:
        print("Invalid input for age. Please enter a number.")
        return

    student_id = input("Enter student ID: ")
    major = input("Enter student's major: ")

    # Create a Student object
    student = Student(name, age, student_id, major)
    student.display_details()

main()
