from weakref import WeakKeyDictionary

class NonNegnative(object):
	""" A descriptor that forbids negative values"""
	def __init__(self, default):
		self.default = default
		self.data = WeakKeyDictionary()

	def __get__(self, instance, owner):
		# we get here when someone calls x.d, and d is a NonNegative instance
		# instance = x
		# value = type(x)
		return self.data.get(instance, self.default)

	def __set__(self, instance, value):
		# we get here when someone calls x.d = val, and d is a NonNegative instance
		# instance = x
		# value = val
		if value < 0:
			raise ValueError("Negative value not allowed: %s" % value)
		self.data[instance] = value

class Movie(object):

	#always put descriptor at the class-level
	rating = NonNegnative(0)
	runtime = NonNegnative(0)
	budget = NonNegnative(0)
	gross = NonNegnative(0)

	def __init__(self, title, rating, runtime, budget, gross):
		self.title = title
		self.rating = rating
		self.runtime = runtime
		self.budget = budget
		self.gross = gross

	def profit(self):
		return self.gross - self.budget

m = Movie('Casablanca', 97, 102, 964000, 1300000)
print m.budget  #calls Movie.budget.__get__(m, Movie)
m.rating = 100  #calls Movie.budget.__set__(m, 100)

try :
	m.rating = -1  #calls Movie.rating.__set__(m, -1)
except ValueError:
	print "Woops, negative value"


class BrokenNonNegative(object):
	def __init__(self, default):
		self.value = default

	def __get__(self, instance, owner):
		return self.value

	def __set__(self, instance, value):
		if value < 0:
			raise ValueError("Negative value not allowed: %s" % value)
		self.value = value

class Foo(object):
	bar = BrokenNonNegative(5)

f = Foo()
g = Foo()

print "f.bar is %s \ng.bar is %s" % (f.bar, g.bar)

f.bar = 10

print "f.bar is %s\ng.bar is %s" % (f.bar, g.bar)



class Descriptor(object):
	def __init__(self, label):
		self.label = label

	def __get__(self, instance, owner):
		print '__get__', instance, owner
		return instance.__dict__.get(self.label)

	def __set__(self, instance, value):
		print '__set__'
		instance.__dict__[self.label] = value

class Foo2(list):
	x = Descriptor('x')
	y = Descriptor('y')

f = Foo2()
f.x = 5
print f.x
print f.__dict__['x']



