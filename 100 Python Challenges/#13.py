#Question 13
#Level 2
'''
Question:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3'''

sentence = input('Please enter a sentence: ')
allLetters = ('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
allDigits = ('0123456789')
counterLetters = 0
counterDigits = 0

for i in range(0, len(sentence)):
    if sentence[i] in allLetters:
        counterLetters += 1
    if sentence[i] in allDigits:
        counterDigits += 1
        
print(f'LETTERS: {counterLetters}')
print(f'DIGITS: {counterDigits}')
