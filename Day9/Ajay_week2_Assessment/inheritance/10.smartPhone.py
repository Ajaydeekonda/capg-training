class Electronics:
    
    def __init__(self,name,price):
        self.name = name
        self.price = price
        
    def display(self):
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")
        
    def dis_usage(self):
        pass
        
class Mobile(Electronics):
    
    def __init__(self,price,type,usage):
        super().__init__("Mobile",price)
        self.type = type
        self.usage = usage
    
    def display(self):
        super().display()
        print(f"Type: {self.type}")
        print(f"Usage: {self.usage}")
        
    def dis_usage(self):
        return print(self.usage)
        
class smartphone(Mobile):
    
    def __init__(self,price,Ram,Rom,CPU,Brand):
        super().__init__(price,"Smartphone","Communication")
        self.Ram = Ram
        self.Rom = Rom
        self.CPU = CPU
        self.Brand = Brand
        
    def dis_usage(self):
        # super().dis_usage()
        return self.usage
    


if __name__ == "__main__":
    
    smartphone1 = smartphone(20000,"4GB","64GB","Snapdragon","Samsung")
    smartphone1.display()
    print(smartphone1.dis_usage())