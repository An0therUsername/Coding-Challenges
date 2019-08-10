#Question 17
#Level 2
'''
Question:
Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
'''

netAmount = 0
print ('Please enter amount or type exit to finish')

while True:
    ri = input()
    if ri == 'exit':
        break 
    transaction = ri.split(' ')
    operation = transaction[0]
    amount = int(transaction[1])
    if operation == 'D':
        netAmount += amount
    elif operation == 'W':
        netAmount -= amount

print(f'You balance is {netAmount}')
