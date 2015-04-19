#! /usr/bin/python

def foo(x,y,z):
	return x+y+z

from functools import partial
f = partial(foo,1,2)
print f(3)

