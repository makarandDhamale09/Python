"""Double Underscore indicates a variable is private"""


# Private access Modifier '__'

class Employee:
    def __init__(self):
        self.__name = "Makarand"


a = Employee()
# print(a.__name) .... cannot be accessed directly
print(a._Employee__name)  # This has been accessed using the name mangling
# print(a.__dir__())


# Protected Access Modifier '_'
class Student():
    def __init__(self):
        self._name = "Makarand"

    def _funName(self):
        return f"This is Protected Method made by {self._name}"


class Subject(Student):
    pass


obj = Student()
obj1 = Subject()
print(dir(obj))
