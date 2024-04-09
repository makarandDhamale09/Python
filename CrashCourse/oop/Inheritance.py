class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.id = emp_id

    def showDetails(self):
        print(f"The name of Employee: {self.id} is {self.name}")


e1 = Employee("Makarand", 400)
e1.showDetails()
e2 = Employee("Rohan", 120)
e2.showDetails()


class Programmer(Employee):
    def __init__(self, name, emp_id, language):
        super().__init__(name, emp_id)
        self.language = language

    def showLanguage(self):
        print(f"The language is {self.language}")


e3 = Programmer("Sam", 100, "Python")
e3.showDetails()
e3.showLanguage()
