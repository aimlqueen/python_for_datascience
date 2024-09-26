class Student:
    def read(self):
        self.name=input("Enter your name:")
        self.mark=float(input("Enter mark:"))
    def grade(self):
        if self.mark>=80:
            print("A grade")
        elif self.mark>=60 and self.mark<80:
            print("B grade")
        elif self.mark>=40 and self.mark<60:
            print("C grade")
        else:
            print("failed")
    def display(self):
        print("Student name:",self.name)
        print("obtained mark:",self.mark)
        print("Your grade is ",self.grade())

s1=Student()
s1.read()
s1.grade()
s1.display()


