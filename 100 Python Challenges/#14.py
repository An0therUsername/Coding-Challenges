#Question 14
#Level 2
'''
Question:
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9'''

sentence = input('Please enter a sentence: ')
counterUpperCase = 0
counterLowercase = 0

for i in range(0, len(sentence)):
    if sentence[i].isupper():
        counterUpperCase += 1
    if sentence[i].islower() :
        counterLowercase += 1
        
print(f'UPPER CASE: {counterUpperCase}')
print(f'LOWER CASE: {counterLowercase}')
