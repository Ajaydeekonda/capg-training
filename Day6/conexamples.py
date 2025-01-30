class Example:
    def __init__(self, name):
        print("First Con")
        
    def __init__(self, age):
        print("Second Con")
        
        
# e = Example(24)

class Example2:
    
    def __init__(self,*args):
        if len(args) == 1:
            print(args[0])
        elif len(args) == 2:
            print(args[0],args[1])
        else:
            print(args)
            
# e2 = Example2(1,2,3,4,5,6,7,8,9,10)


class Example3:
    
    def __init__(self,**kwargs):
        if kwargs.get("name"):
            print(kwargs["name"])
        elif kwargs.get("age"):
            print(kwargs["age"])
        else:
            print(kwargs)
        self.kwargs = kwargs
            
            
    def get_kwargs(self):
        return self.kwargs
    
    
# e3 = Example3(name="Ajay",age=24,location="Hyderabad")

class DestructorExample:
    
    def __init__(self,name):
        self.name = name
        print(f"{self.name} Object Created")
        
    def __del__(self):
        print(f"{self.name} Object Deleted")
        
# d = DestructorExample("destructor")


class anotherEx:
    
    def __init__(self,sname,*args,**kwargs):
        self.sname = sname
        self.args = args
        self.kwargs = kwargs
        
    def get_args(self):
        print(f"{self.sname} Args: {self.args} Kwargs: {self.kwargs}")
        
a = anotherEx(1,2,3,4,5,6,7,8,9,10,name="Ajay",age=24,location="Hyderabad")
print(a.get_args())


    
    

    