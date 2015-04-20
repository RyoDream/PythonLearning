#! /usr/bin/python
import sys

x='foo!!'
sys.stdout.write(x + '\n')

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Arguments List:', str(sys.argv)

list = [ 'abcd', 786 , 2.23, 'john', 70.2 ] 
tinylist = [123, 'john']
print list
print list[0]
print list[1:3]
print list[2:]
print tinylist * 2
print list + tinylist

s = (100,'hehe',300.01)
x,y,z = s
print x
print y
print z




