#!/usr/bin/env python
# encoding: utf-8

clss Times(obejct):
    factor = 1
    @classmethod
    def mul(cls, x):
        return cls.factor * x

class TwoTimes(Times):
    factor = 2

x = TwoTimes.mul(4)
