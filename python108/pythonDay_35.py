#Day 35 : special method / dunder method
#__init__

class MyClass:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"MyClass instance with name:{self.name}"

    def __repr__(self):
        return f"Myclass('{self.name}')"   
obj = MyClass("Alice")

obj1 = MyClass("Tom")
print(str(obj1))
print(repr(obj))


