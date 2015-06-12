#!/usr/bin/env python
# encoding: utf-8

class Account(object):
    num_accounts = 0
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        Account.num_accounts += 1
    def __del__(self):
        Account.num_accounts -= 1
    def deposit(self, amt):
        self.balance += amt
    def withdraw(self, amt):
        self.balance -= amt
    def inquiry(self):
        return self.balance

class EvilAccount(Account):
    def __init__(self, name, balance, evilfactor):
        Account.__init__(self, name, balance)
        self.evilfactor = evilfactor

    def inquiry(self):
        if random.randint(0,4) == 1:
            return self.balance * self.evilfactor
        else:
            return self.balance

class MoreEvilAccount(EvilAccount):
    def deposit(self, amount):
        self.withdraw(5.00)
        super(MoreEvilAccount, self).deposit(amount)
        # EvilAccount.deposit(self, amount)
