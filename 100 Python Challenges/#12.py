#Question 12
#Level 2
'''
Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''

evenDigits = []

for i in range(1000, 3001):
    str_i = str(i)
    if ((int(str_i[0])%2 == 0) and (int(str_i[1])%2 == 0) and (int(str_i[2])%2 == 0) and (int(str_i[3])%2 == 0)):
        evenDigits.append(i)

for i in evenDigits:
    print(str(i))
