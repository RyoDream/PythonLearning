#! /bin/usr/python

import sys
from opus7.container import Container
from opus7.exception import *

class LinkedList(object):

	class Element(object):
		def __init__(self, list, datum, next):
			self._list = list
			self._datum = datum
			self._next = next

		def getDatum(self):
			return self._datum

		datum = property(
			fget = lambda self: self.getDatum()
		)

		def getNext(self):
			return self._next

		next = property(
			fget = lambda self: self.getNext()
		)

		def insertAfter(self, item):
			self._next = LinkedList.Element(
				self._list, item, self._next)
			if self._list._tail is self:
				self._list._tail = self._next

		def insertBefore(self, item):
			tmp = LinkedList.Element(self._list, item, self)
			if self._list._head = self:
				self._list._head = tmp
			else:
				prevPtr = self.__head
				while prevPtr is not None and prevPtr._next is not self:
					prevPtr = prevPtr._next
				prevPtr._next = tmp

	def __init__(self):
		self._head = None
		self._tail = None

	def purge(self):
		"""
		discard the current list contents and make the list empty again
		"""
		self._head = None
		self._tail = None

	def getHead(self):
		return self._head

	head = property(
		fget = lambda self: self.getHead()
	)

	def getTail(self):
		return self._tail

	tail = property(
		fget = lambda self: self.getTail()
	)

	def getIsEmpty(self):
		"""
		:return: bool result which indicates whether the list is empty
		"""
		return self._head is None

	isEmpty = property(
		fget = lambda self: self.getIsEmpty()
	)

	def getFirst(self):
		if self._head is None:
			raise ContainerEmpty
		return self._head._datum

	first = property(
		fget = lambda self: self.getFirst()
	)

	def getLast(self):
		if self._tail is None:
			raise ContainerEmpty
		return self._tail._datum

	last = property(
		fget = lambda self: self.getTail()
	)

	def prepend(self, item):
		"""
		insert an element in front of the first element of the list.
		The prepended element becomes the new head of the list.
		:param item: the value to be prepended to the list
		"""
		tmp = self.Element(self, item, self._head)
		if self._tail is None:
			self._tail = tmp
		self._head = tmp

	def append(self, item):
		"""
		add a new LinkedList.Element at the tail-end of the list
		The appended element becomes the new tail of the list
		:param item: the value to be append to the list
		"""
		tmp = self.Element(self, item, None)
		if self._head is None:
			self._head = tmp
		else:
			self._tail._next = tmp
		self._tail = tmp

	def __copy__(self):
		"""
		:return: the shallow copy of the given list
		"""
		result = LinkedList()
		ptr = self._head
		while ptr != None:
			result.append(ptr._datum)
			ptr = ptr._next
		return result

	def extract(self, item):
		"""
		delete the specified element from the list
		:param item: the element that to be deleted
		"""
		ptr = self._head
		prevPtr = None
		while ptr is not None and ptr._datum is not item:
			prevPtr = ptr
			ptr = ptr._next

		if ptr is None:
			raise KeyError

		if ptr == self._head:
			self._head = ptr._next
		else:
			prevPtr._next = ptr._next

		if ptr == self._tail:
			self._tail = prevPtr

