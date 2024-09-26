#write python program to create student class with constructor
class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id

    def display_details(self):
        print(f"Student Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Student ID: {self.student_id}")

def main():
    students = []
    while True:
        print("\nStudent Registration")
        name = input("Enter student's name (or 'exit' to quit): ")
        if name.lower() == 'exit':
            break
        try:
            age = int(input("Enter student's age: "))
            student_id = input("Enter student ID: ")
        except ValueError:
            print("Invalid input. Age must be a number.")
            continue
        student = Student(name, age, student_id)
        students.append(student)
        print("Student registered successfully!")
    print("\nRegistered Students:")
    for student in students:
        student.display_details()
main()
