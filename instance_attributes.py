'''
    Instance attributes are specific to each object. They are defined within the __init__ method of a class.
'''

class Dog:
    
    def __init__(self,name,age):
        
        self.name = name
        self.age = age
   

dog1 = Dog("Bingo",2)
dog2 = Dog("Rex",3)

print(f'Object 1 {dog1} -- Name:{dog1.name} & Age:{dog1.age}')
print(f'Object 2 {dog2} -- Name:{dog2.name} & Age:{dog2.age}')    
    