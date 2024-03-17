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


