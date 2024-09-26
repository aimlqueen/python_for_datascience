class Parent:
    def add(self):
        a=10
        b=20
        print(a+b)
    def subt(self):
        a=10
        b=20
        print(a-b)

class Child(Parent):
    def mul(self):
        a=10
        b=2
        print(a*b)
    def div(self):
        a=10
        b=2
        print(a/b)

obj=Child()
obj.mul()
obj.div()
obj.add()
obj.subt()