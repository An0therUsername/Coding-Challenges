#Exercise 14 (and Solution)

'''Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

Extras:

Write two different functions to do this - one using a loop and constructing a list, and another using sets.
Go back and do Exercise 5 using sets, and write the solution for that in a different function.'''

#Sample list
list_a = [1,2,4,4,6,5,7,80,23,5,40,8,2,5,23,48,74,80,49,8,9,20]

def remove_dup(a):
    #Using loop and contructing new list
    no_duplicates = []
    for i in a:
        if i not in no_duplicates:
            no_duplicates.append(i)
    return no_duplicates


def remove_dup_set(a):
    #Using sets
    return(list(set(a)))

#Output    
print(list_a)
print(remove_dup(list_a))
print(remove_dup_set(list_a))
