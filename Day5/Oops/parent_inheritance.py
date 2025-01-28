class parent:
    
    def __init__(self):
        self.bigNose = "7CM"
    
    def display_parent(self):
        print("This is the parent class")
        
    
class child(parent):
    def __init__(self):
        super().__init__()
        self.smallNose = "5CM"
    def display_parent(self):
        super().display_parent()
        print("This is the child class")
        
        
        

c = child()
c.display_parent()
print(c.smallNose)