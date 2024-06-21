'''
    Abstraction hides the internal implementation details and only exposes the necessary functionality.
'''

from abc import ABC,abstractmethod

class Animal(ABC):
    
    @abstractmethod
    
    def speak(self):
        pass
    
class Dog(Animal):
    
    def speak(self):
        
        return "uuuuu"
    
class Cat(Animal):
    
    def speak(self):
        
        return "meow"
    

    
    