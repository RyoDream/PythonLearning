#! /usr/bin/python

import Array

a = Array.Array(10, 1)

for i in xrange(10):
	a[i+1] = i

for i in xrange(10):
	print a[i+1]




