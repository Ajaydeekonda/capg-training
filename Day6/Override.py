class Test:
    def __init__(self, roll):
        print(f"First Constructor: roll:{roll}")
    
    def __init__(self, marks):
        print(f"Second Constructor: {marks}")

t = Test(25)

class Example:
    def __init__(self, *args):
        if len(args) == 1:
            print(f"Hello {args[0]}")
        elif len(args) == 2:
            print(f"Hello {args[0]}, you are {args[1]} year old")

e = Example("Bob")
e = Example("Bob", 47)

class Kwargs_Example:
    def __init__(self, studentName, **kwargs):
        self.studentName = studentName
        if "name" in kwargs and "age" in kwargs:
            print(f"Hello {kwargs['name']}, you are {kwargs['age']} years old")
        elif "name" in kwargs:
            print(f"Hello {kwargs['name']}")
        self.xfield = kwargs['name']

obj1 = Kwargs_Example("Hello", name="Alice")
obj2 = Kwargs_Example("CMR", name="Sithara", age=13)
print(obj1.studentName)
print(obj2.studentName)