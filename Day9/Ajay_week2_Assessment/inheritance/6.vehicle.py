class Vehicle:
    
    def __init__(self, type, color, mileage):
        self.type = type
        self.color = color
        self.mileage = mileage
        
    def display(self):
        print("Color:", self.color)
        
    def display_mileage(self):
        print(f"Mileage: {self.mileage}")
        
class Car(Vehicle):
    
    def __init__(self, color, mileage, brand):
        super().__init__("Car", color, mileage) 
        self.brand = brand
        
    def display_mileage(self):
        return super().display_mileage()
        
    def display_brand(self):
        print(f"Brand: {self.brand}")
        
class Bike(Vehicle):
    
    def __init__(self, color, mileage, brand):
        super().__init__("Bike", color, mileage)  # Fixed by removing 'brand' from super
        self.brand = brand
    
    def display_mileage(self):
        return super().display_mileage()
        
    def display_brand(self):
        print(f"Brand: {self.brand}")
        
class ElectricCar(Car):
    
    def __init__(self, color, mileage, brand, battery_capacity):
        super().__init__(color, mileage, brand) 
        self.battery_capacity = battery_capacity
        
    def display_battery_capacity(self):
        print(f"Battery Capacity: {self.battery_capacity}")
        
    def display_brand(self):
        return super().display_brand()
        
    def display_mileage(self):
        return super().display_mileage()
    
    
if __name__ == "__main__":
    
    car_color = input("Enter car color: ")
    car_mileage = input("Enter car mileage: ")
    car_brand = input("Enter car brand: ")

    car = Car(car_color, car_mileage, car_brand)
    car.display()
    car.display_mileage()
    car.display_brand()

    
    bike_color = input("Enter bike color: ")
    bike_mileage = input("Enter bike mileage: ")
    bike_brand = input("Enter bike brand: ")

    bike = Bike(bike_color, bike_mileage, bike_brand)
    bike.display()
    bike.display_mileage()
    bike.display_brand()

   
    ecar_color = input("Enter electric car color: ")
    ecar_mileage = input("Enter electric car mileage: ")
    ecar_brand = input("Enter electric car brand: ")
    ecar_battery_capacity = input("Enter electric car battery capacity: ")

    ecar = ElectricCar(ecar_color, ecar_mileage, ecar_brand, ecar_battery_capacity)
    ecar.display()
    ecar.display_mileage()
    ecar.display_brand()
    ecar.display_battery_capacity()
