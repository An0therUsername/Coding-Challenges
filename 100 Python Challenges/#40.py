'''Question:
Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No". 

Hints:

Use if statement to judge condition.'''

i = input()

if i in ("Yes","YES","yes"):
	print("Yes")
else:
	print("No")

