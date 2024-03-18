#Day 37 Practice implementing classes and oop principle

#exercise 1

class Rectangle:
    def __init__(self,length,  width):
        self.width = width
        self.length = length

    def area(self):
        return self.length * self.width

    def parimeter(self):
        return 2*(self.length + self.width)
    

rect = Rectangle(5,4)
print(rect.area())
print(rect.parimeter())


# Excercise2
import math

class Square(Rectangle):
    def __init__(self,side):
        super().__init__(side,side)

class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius
    
    def perimeter(self):
        return 2* math.pi * self.radius
    
square = Square(5)
print("Square Area:",square.area())
print("Primeter :",square.parimeter())

circle = Circle(3)
print("Circle Area", circle.area())
print("Circle perimeter", circle.perimeter())

