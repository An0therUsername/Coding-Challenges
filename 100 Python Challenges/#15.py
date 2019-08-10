#Question 15
#Level 2
'''
Question:
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106
'''

a = input('Please enter an number: ')
output = int(a) + int(a + a) + int(a + a + a) + int(a + a + a + a)

print(output)
