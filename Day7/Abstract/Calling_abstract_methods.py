from abc import ABC, abstractmethod

class Father(ABC):
    @abstractmethod
    def profession(self):
        print("Father's profession is Business.")
    
    def introduce(self):
        self.profession()

class Engineer(Father):
    def profession(self):
        print("Father's profession is Engineering.")
    
class Doctor(Father):
    def profession(self):
        print("Father's profession is Doctor.")

engineer = Engineer()
doctor = Doctor()
engineer.introduce()
doctor.introduce()