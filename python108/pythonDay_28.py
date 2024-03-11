#Object-Oriented Programming (OOP) Basics

# Classes : A class is a blueprint for creating objects. It defines attributes (data) and methods (functions) that operate on those attributes.
class myClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello , my name is {self.name} and I am {self.age} year old "
    

#Object : An object is an instance of a class. It is created using the class constructor.

obj1 = myClass("TOM", 23)
obj2 = myClass("Jerry", 22)

#accesing attribute and method of object
print(obj1.name)
print(obj1.age)
print(obj2.name, obj2.age)

print(obj1.greet())
print(obj2.greet())
