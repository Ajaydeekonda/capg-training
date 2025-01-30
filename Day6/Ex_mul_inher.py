# class Bird:
#     def fly(self):
#         print("fly with wings")
        
# class mammal:
#     def walk(self):
#         print("walk on legs")

# class bat(Bird,mammal):
#     pass

# b = bat()
# b.fly() 
# b.walk()

class Bird:
    
    hello = "hello"
    
class bird1(Bird):
    hi = "hi"
    age = 20
    
class Bird(bird1):
    def __init__(self):
        print("Bird")
        print(self.hi)
        print(self.hello)
        print(self.age)
        
b = Bird()
