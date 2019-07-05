#Question 2
#Level 1
'''
Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
'''

import timeit

num = int(input('Please enter a number: '))

#1. simple using math.factorial()

import math

def easy_factorial(num):
    return math.factorial(num)
    
#2. manuell (recursiv)

def factorial_recursiv(num):
    if num == 1:
        return num
    else:
        return num * factorial_recursiv(num - 1)

    
#3. manuell

def factorial(num):
    for i in range(1, num):
        num = i * num
    return num
    

print (easy_factorial(num))
print('Execution time for math.factorial(): ' + str(timeit.timeit(lambda : easy_factorial(num))) + ' sec \n')
print(factorial_recursiv(num))
print('Execution time for recursiv function: ' + str(timeit.timeit(lambda : factorial_recursiv(num))) + ' sec \n')
print(factorial(num))
print('Execution time for manuall calculation: ' + str(timeit.timeit(lambda : factorial(num))) + ' sec \n')
