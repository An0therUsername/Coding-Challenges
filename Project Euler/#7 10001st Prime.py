#Problem 7
'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?'''


#from sympy import prime

#print(prime(1001))

primes = []

def isPrime(num):
    prime = True
    for i in primes:
        if num%i == 0:
            prime = False
        else:
            continue
    return prime

i = 2
while len(primes) < 1001:
    if isPrime(i) == True:
        primes.append(i)
    i += 1
     

print(primes[-1:]) #result : 104743
