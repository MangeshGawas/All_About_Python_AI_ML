# Day 30:Contructor and Instances


#__init__ is the initial method as contructor 
class MyClass:
    def __init__(self,arg1,arg2):
        self.attribute1 = arg1
        self.attribute2 = arg2

    
#Instance Variable

class Student:
    def __init__(self,name, age):
        self.name = name
        self.age = age
        #in this name , age are the instances 


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I'am {self.age} year old")

person1 = Person("Tom",23)
person2 = Person("Tom Boi",12)

print(person1.name)
print(person2.name)

        

    