class Addition:
    def add(self, a, b=0, c=0):
        return a + b + c
    
a = Addition()
print(a.add(76))
print(a.add(1, 2))
print(a.add(1, 2, 3))