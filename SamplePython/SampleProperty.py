#! /usr/bin/python

import math

class Circle(object):
	def __init__(self, radius):
		self.radius = radius

	@property
	def area(self):
		return math.pi*self.radius**2

	@property
	def perimeter(self):
		return 2*math.pi*self.radius

c = Circle(4)
print c.radius
print c.area
print c.perimeter

class Foo(object):
	def __init__(self, name):
		self.__name = name

	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, value):
		if not isinstance(value, str):
			raise TypeError("Must be a string!")

		self.__name = value

	@name.deleter
	def name(self):
		raise TypeError("Can't delete name")


