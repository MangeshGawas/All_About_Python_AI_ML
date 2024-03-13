# Day 31: Inheritance ,Subclassing and method overloading

# sublclassing
class Animal:
    def sound(self):
        return "Some generic sound"
    
class Dog(Animal):
    def bark(self):
        return "Woof!"

class Cat(Animal):
    def sound(self): # method overloading Animals
        return "Meow!"
    
dog = Dog()
cat = Cat()

print(dog.bark())
print(cat.sound())