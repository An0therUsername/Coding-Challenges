'''Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].

Hints:

Use map() to generate a list.
Use filter() to filter elements of a list.
Use lambda to define anonymous functions.'''

l = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 , 10]

l_output = list(filter(lambda i: i%2 == 0,map(lambda i: i**2,l)))

print(l_output)
