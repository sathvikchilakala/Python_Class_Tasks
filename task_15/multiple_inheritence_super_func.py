class Parent:
    def __init__(self):
        self.parent_= 'Parent Class'

    def parent_method(self):
        print('Hello')

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.child_ = 'Child Class'


child = Child()

print(child.child_)
print(child.parent_)
child.parent_method()