'''Question:
Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print al l strings line by line.

Hints:

Use len() function to get the length of a string
'''

def printLongestString (s1, s2):
    if len(s1) > len(s2):
        print(s1 + ':' + str(len(s1)))
    elif len(s1) < len(s2):
        print(s2 + ':' + str(len(s2)))
    elif len(s1) == len(s2):
        print(s1 + ':' + str(len(s1)))
        print(s2 + ':' + str(len(s2)))
        
        
printLongestString('Lucy', 'Jan')
printLongestString('Lucy', 'Zebra')
printLongestString('Lucy', 'Goat')
