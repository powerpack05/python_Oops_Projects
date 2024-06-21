'''
    Class attributes are shared among all instances of a class. They are defined outside the __init__ method.
'''

class Dog:
    
    species = "Canis Familiaris"
    
    def __init__(self,name,age):
        
        self.name = name
        self.age = age
        
    
dog1 = Dog("Bruno",3)
dog2 = Dog("Help",4)

print(dog1.species)
print(dog2.species)    
    