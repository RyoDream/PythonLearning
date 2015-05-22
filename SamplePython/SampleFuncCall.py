#! /usr/bin/python

def foo(x,y,z):
	return x+y+z

from functools import partial
f = partial(foo,1,2)
print f(3)

a = 10
def foo(x=a):
	return x

a = 5
print foo() # 10

def foo(x, items=[]):
	items.append(x)
	return items

foo(1)
foo(2)
foo(3)

print foo(4) # [1, 2, 3, 4]

def foo(x, items=None):
	if items is None:
		items = []
	items.append(x)
	return x

foo(1)
foo(2)
foo(3)

print foo(4) # 4

def factor(a):
	d = 2
	while( d <= (a/2)):
		if ((a/d) * d == a):
			return ((a/d),d)
		d = d + 1
	return (a, 1)

print factor(6)     # (3, 2)
print factor(23)    # (23, 1)
print factor(12)    # (6, 2)


def countdown(start):
	n=start
	def display():
		print ('T-minutes %d' % n)
	while n > 0:
		display()
		n -= 1

countdown(5)
