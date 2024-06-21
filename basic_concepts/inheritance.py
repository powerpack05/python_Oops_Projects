'''
    Inheritance allows a class to inherit attributes and methods from another class.
'''

class Animal:
    
    def __init__(self,name):
        
        self.name = name
        
    def speak(self):
        pass
    
class Dog(Animal):
    
    def speak(self):
        return 'uuuuuuu'
    
class Cat(Animal):
    
    def speak(self):
        
        return 'meow'
    
dog = Dog("Buddy")
cat = Cat("Cat")

print(dog.speak())
print(cat.speak())