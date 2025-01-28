class Car:
    def __init__(self,brand,model):
        self.model = model
        self.brand = brand

    def display_info(self):
        print(f"This car is {self.brand}, model:{self.model}")
        
Car1 = Car("Suzuki", "Vitara Brezza")
Car2 = Car("Tata", "Indica")

print(f'{Car1.brand},{Car1.model}')