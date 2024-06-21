'''
    Magic methods are special methods in Python that start and end with double underscores (__). They enable the use of built-in functions and operators.
'''

class Book:
    
    def __init__(self,title,author):
        
        self.title = title
        self.author = author
        
    def __str__(self):
        
        return f'{self.title} by {self.author}'
    
book = Book("1988","George Well")
print(book)