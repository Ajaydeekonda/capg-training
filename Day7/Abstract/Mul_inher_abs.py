from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def get_name(self):
        print("Person's name is John Doe")

class Employee(ABC):
    @abstractmethod
    def get_salary(self):
        print("Employee's salary is $1000")

class Manager(Person, Employee):
    def get_name(self):
        return super().get_name()
    def get_salary(self):
        return super().get_salary()
    
manager = Manager()
manager.get_name()
manager.get_salary()