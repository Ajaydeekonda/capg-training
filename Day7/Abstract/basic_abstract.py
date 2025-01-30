from abc import ABC, abstractmethod

class Animal(ABC):  # This is an abstract class
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Dog sound's like Bark!")

class Cat(Animal):
    def make_sound(self):
        print("Cat sound's like Meow!")

dog = Dog()
dog.make_sound()
cat = Cat()
cat.make_sound()