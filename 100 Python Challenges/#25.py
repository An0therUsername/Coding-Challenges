#Question 25
#Level 1
'''
Question:
    Define a class, which have a class parameter and have a same instance parameter.

Hints:
    Define a instance parameter, need add it in __init__ method
    You can init a object with construct parameter or set the value later
    
    '''
    
class Labortory:
    
    test = 'a animal experiment'
    
    def __init__(self, test = None):
        self.test = test
    
    def __str__(self):
        return f'a {self.test} experiment'
    
t1 = Labortory.test
t2 = Labortory('mice')
t3 = Labortory('human')
print(t1)
print(t2)
print(t3)
