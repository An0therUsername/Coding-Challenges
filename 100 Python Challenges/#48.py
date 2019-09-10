'''Question:
Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area. 

Hints:

Use def methodName(self) to define a method.'''


from math import pi

class Circle (object):
	def __init__(self, r):
		self.radius = r
		
	def calcArea(self):
		return self.radius**2*pi
		

print(Circle(80).calcArea())
