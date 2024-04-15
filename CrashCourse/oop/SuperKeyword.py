class ParentClass:
    def parent_method(self):
        print("This is a parent Method")


class ChildClass(ParentClass):
    def parent_method(self):
        print("This is parent method in child class")

    def child_method(self):
        print("This is a child method")
        super().parent_method()


child = ChildClass()
child.child_method()
child.parent_method()
