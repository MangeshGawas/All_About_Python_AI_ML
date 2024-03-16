#Day 33
#Encapsulation and Access modifier

class Car:
    def __init__(self,brand , model):
        self._brand = brand #Protected Attribute
        self.__model = model #Privare Attribute

    def drive(self):
        return f"Driving {self._brand} {self.__model}"
    
    #access modifier
    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self,value):
        self.__model = value
    
car1 = Car("Toyota", "Corolla")
print(car1._brand) #It will be printing
# print(car1.__model) #Attribute error since model is a private attribute

#access modifier
car = Car("Tata", "Nexon")
print(car.model)
car.model = "Tiago"
print(car.model)