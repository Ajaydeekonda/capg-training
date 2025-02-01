class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def move(self):
        print(f"The {self.make} {self.model} drives on the road.")

class Airplane:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def move(self):
        print(f"The {self.make} {self.model} flies in the air.")


class FlyingCar(Car, Airplane):
    def __init__(self, make, model, has_wings):
        Car.__init__(self, make, model) 
        Airplane.__init__(self, make, model)  
        self.has_wings = has_wings

    def move(self):
        if self.has_wings:
            print(f"The {self.make} {self.model} is flying in the air.")
        else:
            print(f"The {self.make} {self.model} is driving on the road.")


flying_car = FlyingCar("Tesla", "Model X", True)
flying_car.move()
