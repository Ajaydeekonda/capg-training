class shape:
    def area(self):
        pass
    
class circle(shape):
    
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
    
class square(shape):
    
    def __init__(self,side):
        self.side = side
        
    def area(self):
        return self.side ** 2
    
class rectangle(shape):
    
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
        
    def area(self):
        return self.length * self.breadth

    
c = circle(5)
print(c.area())
s = square(5)
print(s.area())
r = rectangle(5,6)
print(r.area())