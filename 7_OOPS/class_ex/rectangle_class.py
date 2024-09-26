class Rectangle:
    def set_side(self, x, y):
        self.height = x
        self.width = y
        print(f"Height is {self.height} cm and width is {self.width} cm")
    def area(self):
        return self.height * self.width
    def perimeter(self):
        return 2 * (self.height + self.width)

rect = Rectangle()
rect.set_side(5, 3)
print(f"Area is {rect.area()} cm")
print(f"Perimeter is {rect.perimeter()} cm")
