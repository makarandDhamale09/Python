class Math:
    def __init__(self, num):
        self.__num = num

    def add_to_num(self, num1):
        self.__num += num1

    @staticmethod
    def add(a, b):
        return a + b

    @property
    def num(self):
        return self.__num


math = Math(3)
math.add_to_num(4)
print(math.num)
print(Math.add(4, 4))


# Static variables
class Employee: 
    name = "Makarand"


emp = Employee()
print(Employee.name)