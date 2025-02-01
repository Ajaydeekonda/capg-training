from typing import List


class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def display_details(self):
        print("Name:",self.name)
        print("Age:",self.age)
    
    
class Employee(Person):
    
    def __init__(self, name, age, id, department, salary,role):
        super().__init__(name, age)
        self.id = id
        self.department = department
        self.salary = salary
        self.role = role
        
    def display_details(self):
        super().display_details()
        print("Employee ID:",self.id)
        print("Employee Department:",self.department)
        
    def get_salary(self):
        return self.salary
    
    def work(self):
        return f"{self.name} is working as {self.role}"
        
    
    
class Manager(Employee):
    
    def __init__(self,name,age,id,department,salary):
        super().__init__(name,age,id,department,salary,"Manager")
        self.employee_list: List[Employee] = []
        
    def hire(self,employee):
        print(f"{employee.name} has been hired.")
        self.employee_list.append(employee)
    
    def fire(self,employee):
        print(f"{employee.name} has been fired.")
        self.employee_list.remove(employee)
        
    def approve_leave(self,employee):
        print(f"{employee.name} has been granted leave.")
        

if __name__ == "__main__":
    manager = Manager("Alice", 40, "M001", "Management", 100000)
    
    emp = Employee("John", 25, "E101", "IT", 50000, "Developer")
    emp1 = Employee("Doe", 30, "E102", "HR", 60000, "HR")
    emp2 = Employee("Jane", 35, "E103", "Finance", 70000, "Finance")
    manager.hire(emp)
    manager.hire(emp1)
    manager.hire(emp2)
    manager.approve_leave(emp)
