'''Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)'''



# Collecting used data
name = input('Please enter your name: ')
age = input('Please tell me your age: ')
repeats = input('How many times shall I answer? ')
x = 1

# Calculate years to 100
years = 100 - int(age)

# Print personalised answer multiple times
while x <= int(repeats):
    x += 1
    print('Hi ' + name.title() + ', you will reach the age of 100 in ' + str(years) + ' years.')




