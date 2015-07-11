from abc import ABCMeta, abstractmethod, abstractproperty

class Foo:
	__metaclass__ = ABCMeta

	@abstractmethod
	def spam(self, a, b):
		pass

	@abstractproperty
	def name(self):
		pass

class Grok(object):
	def spam(self, a, b):
		print ("Grok.spam")

Foo.register(Grok)

