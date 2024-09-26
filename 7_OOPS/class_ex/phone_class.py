class Phone:
    def read(self):
        self.name=input("Enter name:")
        self.display_size=input("Enter display size:")
        self.color=input("Enter color:")
        self.weight=int(input("Enter weight:"))
    def display(self):
        print(f"name:{self.name}")
        print(f"display_size:{self.display_size}")
        print(f"color:{self.color}")
        print(f"weight:{self.weight}")
p1=Phone()
p1.read()
p1.display()
p2=Phone()
p2.read()
p2.display()

