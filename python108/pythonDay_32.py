'''
Polymorphism:

Polymorphism allows objects of different classes to be treated as objects of a common superclass. It enables flexibility and extensibility in object-oriented design.

'''
class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"
    
class Cat(Animal):
    def sound(self):
        return "Meow!!"
    
def make_sound(animal):
    return animal.sound()

dog = Dog()
cat = Cat()
print(make_sound(dog)) 
print(make_sound(cat)) 

# Method 
class Calculator:
    def add(self,a , b=0):
        return a + b
    
#method overloading with default parameter value
calc = Calculator()
print(calc.add(2))
print(calc.add(2,3))
