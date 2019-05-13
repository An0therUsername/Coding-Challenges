#Exercise 20 (and Solution)
'''
Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

Extras:

Use binary search.'''

import random

list = [i for i in range(1,10)]
number = random.randint(1,20)

def isInList (list, number):
    if number in list:
        return True
    else:
        return False
        
print(isInList(list, number))
print('because %s was the number. The list has the values 1-9.' %(number))
