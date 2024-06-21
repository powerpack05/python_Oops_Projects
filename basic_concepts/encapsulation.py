'''
    Encapsulation restricts access to certain components. Attributes can be made private by prefixing them with an underscore (_).
'''

class Dog:
    
    def __init__(self,name,age):
        
        self._name = name
        self._age = age
    
    def get_name(self):
        
        return self._name
    
    def set_name(self,name):
        
        self._name = name
        
dog = Dog("Buddy", 3)
print(dog.get_name())  # Buddy
dog.set_name("Lucy")
print(dog.get_name())  #