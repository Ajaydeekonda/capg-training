class Animal:
    def sound(self):
        return "Venkat Bhai Bolthey!"
    
class Dinosaur(Animal):
    def sound(self):
        return "Woahhhhh!"

class Hippo(Animal):
    def sound(self):
        return "Hahahaha!"
    
animals = [Dinosaur(), Hippo()]
for a in animals:
    print(a.sound())

print(Animal().sound())