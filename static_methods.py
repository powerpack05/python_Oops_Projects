'''
    Static methods do not access instance or class attributes. They are defined using the @staticmethod decorator.
'''

class Math:
    
    @staticmethod
    def add(a,b):
        
        return a+b
    
print(Math.add(2,3))