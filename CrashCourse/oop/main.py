from AccessModifiers import Student, Employee


class Person:
    # Args constructor where self is mandatory
    def __init__(self, name, occ):
        self.name = name
        self.occ = occ

    def info(self):
        print(f"{self.name} is a {self.occ}")


a = Person("Makarand", "Developer")
b = Person("Priyal", "Tester")

a.info()
b.info()


# Decorators in Python

# greet is a higher order function that takes function s a parameter
def greet(fx):
    def mfx():
        print("This is modify function")
        fx()
        print("End of Modify function")

    return mfx


@greet  # We have decorated the hello method with greet annotation.
def hello():
    print("Hello")


hello()


# Getters and Setters
class MyClass:
    def __init__(self, value):
        self._value = value

    # A getter value is created with @property annotation which helps in fetching the value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value


obj = MyClass(10)
print(obj.value)  # Accessing _value is not possible as it is protected
# obj.value = 12 ... cannot set a value with the property annotation also need a setter annotation
obj.value = 12
print(f"Modified Value : {obj.value}")

obj = Student()
print(obj._name)

obj1 = Employee()

# This will show you all the variables available in obj1
print(dir(obj1))

# name Mangling to display private variables
print(f"Value : {obj1._Employee__name}")
