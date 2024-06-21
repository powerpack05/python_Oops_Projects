'''
    Class methods access class attributes. They are defined using the @classmethod decorator.
'''

class Dog:
    
    species = "Canis Familiaris"
    
    def __init__(self,name,age):
        
        self.name = name
        self.age = age
        
    @classmethod
    def common_species(cls):
        
        return cls.species
    
    
print(Dog.common_species())