#! /usr/bin/python

class JustCounter:
	__secretCount = 0

	def count(self):
		self.__secretCount += 1
		print self.__secretCount

count = JustCounter()
count.count()
count.count()

print count._JustCounter__secretCount
print count.__secretCount

