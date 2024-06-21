'''
    Polymorphism allows methods in different classes to have the same name but behave differently.
'''

class Animal:
    
    def speak(self):
        
        pass
    
    
class Dog(Animal):
    
    def speak(self):
        return "uuuuu"
    
class Cat(Animal):
    
    def speak(self):
        return "meow"
    
    
# dog = Dog()
# cat = Cat()

# print(dog.speak())
# print(cat.speak())

animals = [Dog(),Cat()]

for animal in animals:
    
    print(animal.speak())
