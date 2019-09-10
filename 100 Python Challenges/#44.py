'''Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).

Hints:

Use filter() to filter elements of a list.
Use lambda to define anonymous functions.'''

from random import randint

l = [randint(1,30) for i in range(1,20)]

l_even = list(filter(lambda i: i%2 == 0 and i <= 20, l))

print(l_even)
