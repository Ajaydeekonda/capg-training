class Employee:
    
    def __init__(self,name,salary):
        self.__name = name
        self.__salary = salary
    
    def get_name(self):
        return self.__name
    
    def get_salary(self):
        return self.__salary
    
    def set_name(self,name):
        self.__name = name
        
    def set_salary(self,sal):
        self.__salary = sal
        
emp1 = Employee("Ajay", 100000)
print(emp1.get_name())  
print(emp1.get_salary())
emp1.set_name("Rahul")
emp1.set_salary(200000)
print(emp1.get_name())
print(emp1.get_salary())