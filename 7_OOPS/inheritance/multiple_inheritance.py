class Mother:
    def sample(self):
        print("this is mother - sample class")
class Father:
    def test(self):
        print("this is father - test class")
class Son(Mother,Father):
    def son(self):
        print("this is son")

obj=Son()
obj.sample()
obj.test()
obj.son()

