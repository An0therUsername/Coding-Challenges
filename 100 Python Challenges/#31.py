'''
Question:
Define a function that can accept an integer number as input and print the "It is an even number" if the number is even, otherwise print "It is an odd number".

Hints:

Use % operator to check if a number is even or odd.

'''

def isEven(x):
    if x == 0:
        print('Number is 0')
    elif x%2 == 0:
        print(str(x) + ' is an even number')
    else:
        print(str(x) + ' is an uneven number')


isEven(6)
isEven(27)
