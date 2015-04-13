#! /usr/bin/python

class Array(object):

	# _data is a Python list
	# _baseIndex is a integer which records the lower bound for array indices


	def __init__(self, length = 0, baseIndex = 0):
		"""
		When a list is allocated, two things happen.
		1. Memory is allocated for the list object and its elements.
		2. Each element of the list is initialized with the appropriate default value.
		"""
		assert length >= 0
		self._data = [None for i in xrange(length)]
		self._baseIndex = baseIndex

	def __copy__(self):
		"""
		The __copy__ method creates a shallow copy.
		A shallow copy creates a copy of the Array object but does not copy the objects contained in the array.
		If the object provides a __copy__ method, the copy function calls that method to create the copy.
		The elements of the two array are shared.
		"""
		result = Array(len(self._data))
		for i, datum in enumerate(self._data):
			result._data[i] = datum
		result._baseIndex = self._baseIndex
		return result

	def getOffset(self, index):
		offset = index - self._baseIndex
		if offset < 0 or offset >= len(self._data):
			raise IndexError
		return offset

	def __getitem__(self, index):
		return self._data[self.getOffset(index)]

	def __setitem__(self, index, value):
		self._data[self.getOffset(index)] = value

	def getData(self):
		return self._data

	data = property(
		fget = lambda self: self.getData()
	)

	def getBaseIndex(self):
		return self._baseIndex

	def setBaseIndex(self, baseIndex):
		self._baseIndex = baseIndex

	baseIndex = property(
		fget = lambda self: self.getBaseIndex(),
	    fset = lambda self, value: self.setBaseIndex(value)
	)

	def __len__(self):
		return len(self._data)

	def setLength(self, value):
		if (len(self._data) != value):
			newData = [None for i in xrange(value)]
			m = min(len(self._data), value)
			for i in xrange(m):
				newData[i] = self._data[i]
			self._data = newData

	length = property(
		fget = lambda self: self.__len__(),
	    fset = lambda self, value: self.setLength(value)
	)

a = Array(10, 1)

for i in xrange(10):
	a[i+1] = i
	print a[i+1]

b = a.getOffset(8)
print b