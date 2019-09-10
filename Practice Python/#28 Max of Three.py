#Exercise 28 (and Solution)
''''
Implement a function that takes as input three variables, and returns the largest of the three. Do this without using the Python max() function!

The goal of this exercise is to think about some internals that Python normally takes care of for us. All you need is some variables and if statements!'''

def return_max(a,b,c):
	if a > b and a > c:
		return a
	if b > a and b > c:
		return b
	if c > a and c > b:
		return c
		
return_max(4,7,8)
return_max
