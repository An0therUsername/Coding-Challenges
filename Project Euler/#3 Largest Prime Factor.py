'''The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?'''

#List divisors

from functools import reduce 
#had to look up the best way to multiply all elements in a list

num = 600851475143
divisors = []
x = 2

while x < int(num):
    if int(num) %x == 0:
        divisors.append(x)
        multm = reduce(lambda x, y: x*y, divisors) 
        if multm == num:
            break
    x += 1
    
print(divisors)
