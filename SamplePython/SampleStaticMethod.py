#!/usr/bin/env python
# encoding: utf-8

class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @staticmethod
    def now():
        t = time.localtime()
        return Date(t.tm_year, t.tm_month, t.tm_day)

    @staticmethod
    def tomorrow():
        t = t.localtime(time.time() + 86400)
        return Date(t.tm_year, t.tm_month, t.tm_day)

a = Date(2015, 6, 12)
b = Date.noew() # call static method now()
c = Date.tomorrow() # call static method tomorrow()


