#!/usr/bin/env python
# encoding: utf-8

class Complex(object):
    def __init__(self, real, imag=0):
        self.__real = float(real)
        self.__imag = float(imag)

    @property
    def real(self):
        return self.__real

    @property
    def imag(self):
        return self.__imag

    @real.setter
    def real(self, value):
        self.__real = float(value)

    @imag.setter
    def imag(self, value):
        self.__imag = float(value)

    def __repr__(self):
        return "Complex(%s,%s)" % (self.__real, self.__imag)

    def __str__(self):
        return "(%g+%gj)" % (self.__real, self.__imag)

    def __add__(self, other):
        if not isinstance(other, Complex):
            raise TypeError("Must be a Complex")
        return Complex(self.__real + other.real, self.__imag + other.imag)

    def __sub__(self, other):
        if not isinstance(other, Complex):
            raise TypeError("Must be a Complex")
        return Complex(self.__real - other.real, self.__imag - other.imag)

c = Complex(2,3)
d = Complex(4,4)

print c
print d
print c+d
print d-c
print c+4



