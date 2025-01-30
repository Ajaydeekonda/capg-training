from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def area(self, length, breadth):
        return length * breadth
    
class Circle(Shape):
    def area(self, radius):
        return 3.14 * radius * radius
    
rectangle = Rectangle()
print(f"Area of Rectangle: {rectangle.area(10, 20)}")
circle = Circle()
print(f"Area of Circle: {circle.area(10)}")