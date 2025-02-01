class Animal():
    
    def speak(self):
        print("Animal is speaking")
        
class Dog(Animal):
    
    def speak(self):
        print("Dog is barking")
        
class Cat(Animal):
    
    def speak(self):
        print("Cat is meowing") 
        
if __name__ == "__main__":
    animal = Animal()
    animal.speak()
    dog = Dog()
    dog.speak()
    cat = Cat()
    cat.speak()


