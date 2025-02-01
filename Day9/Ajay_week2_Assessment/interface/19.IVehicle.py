from abc import ABC, abstractmethod

class IVehicle(ABC):
    
    @abstractmethod
    def start_engine(self):
        pass
    
    @abstractmethod
    def stop_engine(self):
        pass
    
class Car(IVehicle):
    
    def start_engine(self):
        print("Car: Starting engine")
        
    def stop_engine(self):
        print("Car: Stopping engine")
        
class Bike(IVehicle):
    
    def start_engine(self):
        print("Bike: Starting engine")
        
    def stop_engine(self):
        print("Bike: Stopping engine")
        
class Truck(IVehicle):
    
    def start_engine(self):
        print("Truck: Starting engine")
        
    def stop_engine(self):
        print("Truck: Stopping engine")
        
        
if __name__ == "__main__":
    
    car = Car()
    car.start_engine()
    car.stop_engine()
    
    bike = Bike()
    bike.start_engine()
    bike.stop_engine()
    
    truck = Truck()
    truck.start_engine()
    truck.stop_engine()