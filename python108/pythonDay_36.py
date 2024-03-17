#Day 35 : Class Inheritance and composition

#class Inheritance
class Animal:
    def speak(self):
        return "Animals Speak"
    
class Dog(Animal):
    def bark(self):
        return "Woof"
    
dog = Dog()
print(dog.speak())

print(dog.bark())


# class Composition
class Engine:
    def start(self):
        return "Engine Started"
    
class Car:
    def __init__(self):
        self.engine =Engine()

    def drive(self):
        return self.engine.start()+ " and car is driving"
    
car = Car()
print(car.drive())
