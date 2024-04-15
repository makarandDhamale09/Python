### 'Python' course 100 days Challenge

To write the code block

```Python
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
```

This is how a code block is added in Readme.md file.

We provide the name of the language at the top and the code will be highlighted accordingly