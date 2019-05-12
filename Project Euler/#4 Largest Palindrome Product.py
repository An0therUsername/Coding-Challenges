#Problem 4

'''A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.'''

def reverse_number(n):
    '''Reverse number'''
    return n[::-1]    

def is_palindrome(n):  
    '''Check if n is a palindrome'''     
    if str(n) == reverse_number(str(n)):
        return True

def multiples_of_3_digits():
    """Return all numbers that are the product of two 3-digit numbers"""
    multiples = []
    x = 100
    y = 100
    while x < 1000:
        while y < 1000:
            w = x*y
            multiples.append(w)
            y += 1
        y=100
        z = x*y
        multiples.append(z)
        x += 1
    return multiples

def main(nums):
    '''Checks list against palindrom function and prints largest palindrom'''
    p_list = []
    for i in nums:
        if is_palindrome(i) == True:
            p_list.append(i)
    print(max(p_list))
       
main(multiples_of_3_digits())
