'''Exercise 2 (and Solution)

Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.'''

#Ask User for number
num = input('Please enter a number: ')
check = input('Please enter a second number: ')

#Answer appropriatly depending on even/odd
if int(num)%4 == 0:
    print(num + ' is even and a multiple of 4.')
elif int(num)%2 == 0:
    print(num + ' is an even number.')
else:
    print(num + ' is an uneven number.')

#Answer if num is a multiple of check        
if int(num)%int(check) == 0:
    print(num + ' is a multiple of ' + check)
else:
    print(num + ' is a not multiple of ' + check)
