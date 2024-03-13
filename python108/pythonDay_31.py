# Day 31: Inheritance ,Subclassing and method overloading

# sublclassing
class Animal:
    def sound(self):
        return "Some generic sound"
    
class Dog:
    def bark(self):
        return "Woof!"

class Cat:
    def sound(self): # method overloading Animals
        return "Meow!"
    
dog = Dog()
cat = Cat()