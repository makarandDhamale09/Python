"""The work of Dunder Methods or Magic Methods for some special purpose
hence called as Magic methods"""


class Employee:
    name = "Makarand"

    def __len__(self):
        """This is a dunder method that starts and ends with '__'"""
        i = 0
        for c in self.name:
            i += 1
        return i


e = Employee()
print(e.name)
print(len(e))


# Method Overriding
class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(radius, radius)

    def area(self):
        return 3.14 * super().area()


rec = Shape(3, 5)
print(f"Area : {rec.area()}")
circle = Circle(4)
print(f" Area : {circle.area()}")
