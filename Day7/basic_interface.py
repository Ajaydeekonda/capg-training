from abc import ABC, abstractmethod

class Animal(ABC):
    
    @abstractmethod
    def make_sound(self):
        pass
    
class Dog(Animal):
    
    def make_sound(self):
        print("Dog barks")

dog = Dog()
dog.make_sound()
# Output: Dog barks