from abc import ABC, abstractmethod
class Ishape(ABC):
    
    @abstractmethod
    def calculate_area(self):
        pass
    
class Rectangle(Ishape):
    
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
        
    def calculate_area(self):
        return self.length * self.breadth
    
class Circle(Ishape):
    
    def __init__(self,radius):
        self.radius = radius
        
    def calculate_area(self):
        return 3.14 * self.radius * self.radius
    
if __name__ == "__main__":
    
    r = Rectangle(10,20)
    print(r.calculate_area())
    
    c = Circle(10)
    print(c.calculate_area())