class Car:
  def __init__(self, name, model, year):
    self.name = name
    self.model = model
    self.year = year

  def function(self):
    print("This is a class method")


obj = Car("Toyota", "Corolla", 2020)
print(obj.name)
print(obj.model)