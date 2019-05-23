# Problem 5
'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

# LCM = Least Common Multiplier
# GCD = Greatest Common Divisor

import math

r = 1

for i in range(2,21):
    r = r*i//math.gcd(r,i)
    
print(r)
