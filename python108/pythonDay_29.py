#  Defining classes, attributes, and methods.


#define a class
class myClass:
    pass

#defining Attribute

# 1)Using Constructor

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 2)Direct within class
class Car:
    brand = "Toyoto"
    model = "Corolla"

###########
#defining Method

class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2
    

########################################
#Example: Using Defined Class, Attributes, and Methods:
class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age
    def greet(self):
        return f"Hello Im {self.name} and I'm {self.age} year old "
    
person1 = Person("Mangesh", 25)

print(person1.greet())
