#Question 20
#Level 3
'''
Question:
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

Hints:
Consider use yield
'''

def iterate(number):
    i = 1
    div_by_seven = []
    while i < number:
        if i%7 == 0:
            div_by_seven.append(i)
        i += 1
    print(div_by_seven)
    
iterate(100)
