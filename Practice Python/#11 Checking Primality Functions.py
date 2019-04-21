#Exercise 11 (and Solution)

'''Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, described below.'''


#Version 1 (without functions)

'''while True:

    x=2
    divisors = []
    
    num = input('Test if your number is prime. Press (e) to exit. Your number? ')
    if num == 'e':
        print('terminaring')
        break
    
    while x < int(num):
        if int(num) %x == 0:
            divisors.append(x)
        x += 1
    
    if len(divisors) <= 1:
        print('Hooray!!! Your number is prime')
    else:
        print('\nYour number is not prime. It can be divided by ' + str(divisors) + '.\n')'''
    
    
#Version 2 (with functions)


def get_input(prompt):
    return int(input(prompt))

def build_divisors(num):
    divisors = [x for x in range(2,num) if num % x == 0]
    return divisors
           
def check_prime(divisors):
    if len(divisors) <= 0:
        prime = True
    else:
        prime = False
    return prime
    
def print_response(prime):
    if prime == True:
        print('Prime.\n')
    else:
        print('Not prime. Can be divided by ' + str(build_divisors(num)) + '\n')
    
while True:
    num = get_input('Enter a number or (0) to exit: ')
    if num == 0:
        print('terminating...bye')
        break
    else:
        print_response(check_prime(build_divisors(num)))
    
