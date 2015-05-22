#! /usr/bin/python

a = 42
b = 13.142783
c = "hello"
d = {'x': 13, 'y': 1.5432, 'z': 'world'}
e = 1234567890123456

r = "a is %d" % a
print r

r = "%10d %f" % (a, b)
print r

r = "%+010d %E" % (a, b)
print r

r = "%(x)-10d %(y)0.3g" % d
print r

r = "%0.3s %s" % (c, d['z'])
print r

r = "%*.*f" % (0, 3, b)
print r

r = "%*.*f" % (10, 3, b)
print r

r = "e = %d" % e
print r

r = "{0} {1} {2}".format('Goog', 100, 499.10)
r = "{name} {shares} {price}".format(name='Goog', price=490.10, shares=100)
r = "Use {{ and }} to output single curly braces".format()

stock = { 'name' : 'Ryo',
          'shares': 100,
          'price': 499.10}

r = '{0[name]} {0[shares]} {0[price]}'.format(stock)
print r

x = 3 + 4j
r = '{0.real} {0.imag}'.format(x)
print r

