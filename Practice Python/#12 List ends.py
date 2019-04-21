#Exercise 12 (and Solution)

'''Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.'''

a = [5, 10, 15, 20, 25]
b = [6, 9, 6, 3, 2, 6, 20, 89]

def make_new_list(list):
    new_list = [list.pop(0),list.pop(-1)]
    print(new_list)
    
make_new_list(a)
make_new_list(b)
