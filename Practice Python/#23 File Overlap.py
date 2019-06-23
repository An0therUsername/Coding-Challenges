#Exercise 23 (and Solution)
'''
Given two .txt files that have lists of numbers in them, find the numbers that are overlapping. One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of happy numbers up to 1000.

(If you forgot, prime numbers are numbers that can’t be divided by any other number. And yes, happy numbers are a real thing in mathematics - you can look it up on Wikipedia. The explanation is easier with an example, which I will describe below.)'''

prime = 'primenumbers.txt'
happy = 'happynumbers.txt'


def openFile(filename):
    with open(filename, 'r') as f:
        numberlist = []
        for number in f.readlines():
            number = int(number.rstrip('\n'))
            numberlist.append(number)
        return numberlist


def findDuplicates(l1, l2):
    dubs = []
    for n in l1:
        if n in l2:
            dubs.append(n)
    return dubs


print(f'The duplicates of {prime} and {happy} are:')
print(findDuplicates(openFile(prime), openFile(happy)))

