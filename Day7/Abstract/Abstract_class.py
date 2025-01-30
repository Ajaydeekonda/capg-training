from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def max_speed(self):
        pass

    def __init__(self,brand):
        self.brand = brand

class Car(Vehicle):
    
    def max_speed(self):
        print(f"{self.brand} car's max speed is 150 km/hr")

class Bike(Vehicle):
    
    def max_speed(self):
        print(f"{self.brand} bike's max speed is 120 km/hr")   

car = Car("Toyota")
car.max_speed()
bike = Bike("Honda")
bike.max_speed()