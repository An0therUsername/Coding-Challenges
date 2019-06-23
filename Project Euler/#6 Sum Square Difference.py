#Problem 6
'''
The sum of the squares of the first ten natural numbers is,

1 hoch 2 + 2 hoch 2 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.'''

import math

def create_List():
    number_list = [i for i in range(1,101)]
    return number_list

def return_Sum_of_Squares(number_list):
    squares = []
    for i in number_list:
        squares.append(int(math.pow(i, 2)))
    return sum(squares)

def return_Square_of_Sum(number_list):
    return int(math.pow(sum(number_list), 2))
    
    
number_list = create_List()    
print(return_Square_of_Sum(number_list) - return_Sum_of_Squares(number_list))
