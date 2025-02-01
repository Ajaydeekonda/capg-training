class shape:
    def area(self):
        pass
    
class Traingle(shape):
    def __init__(self,base,height):
        self.base = base
        self.height = height
        
    def area(self):
        return 0.5 * self.base * self.height
    
class square(shape):
    def __init__(self,side):
        self.side = side
        
    def area(self):
        return self.side * self.side
    
if __name__ == "__main__":
    
    t = Traingle(10,20)
    print(t.area())
    
    s = square(10)
    print(s.area())