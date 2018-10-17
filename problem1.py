# Manny Pagan
# Sept 24th Python Course
# Assignment 6
# Due: Oct 17th


class BankAccount:
    def __init__(self, balance=0.00, interest_rate=0.02):
        self.interest_rate = interest_rate
        self.balance = balance
    def withdraw(self, amount):
        self.balance = self.balance - amount
        return self.balance
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance
    def accumulate_interest(self):
        self.balance = self.balance + (self.balance * self.interest_rate)
        return self.balance

class ChildrensAccount:
    def __init__(self, balance=0.00, interest_rate=0.00):
        self.interest_rate = interest_rate
        self.balance = balance
    def withdraw(self, amount):
        self.balance = self.balance - amount
        return self.balance
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance
    def accumulate_interest(self):
        self.balance = (self.balance + 10.00)
        return self.balance

class OverdraftAccount:
    def __init__(self, balance=0.00, interest_rate=0.02):
        self.interest_rate = interest_rate
        self.balance = balance
    def withdraw(self, amount):
        if amount < 0.00:
            return False
        else:
            pass
        if (self.balance - amount) <= 0.00:
            self.balance = (self.balance - 40.00)
            return self.balance
        else:
            self.balance = (self.balance - amount)
            return self.balance
    def deposit(self, amount):
        if amount < 0.00:
            return False
        else:
            self.balance = self.balance + amount
            return self.balance
    def accumulate_interest(self):
        if self.balance >= 0.00:
            self.balance = (self.balance * 1.02)
            return self.balance
        if self.balance <= 0.00:
            self.interest_rate = 0.00
            return self.balance
        else:
            pass
    def overdraft_penalty(self):
        if (self.balance - 40.00) <= 0.00:
            return False
        else:
            self.balance = (self.balance - 40.00)
            return self.balance
    def no_interest(self):
        if self.balance <= 0.00:
            self.interest_rate = 0.00
        else:
            pass

print()
print('----- BankAccount:')
print()

basic_account = BankAccount()
basic_account.deposit(600)
print("Basic account has ${}".format(basic_account.balance))
basic_account.withdraw(17)
print("Basic account has ${}".format(basic_account.balance))
basic_account.accumulate_interest()
print("Basic account has ${}".format(basic_account.balance))

print()
print('----- ChildrensAccount:')
print()

childs_account = ChildrensAccount()
childs_account.deposit(34)
print("Child's account has ${}".format(childs_account.balance))
childs_account.withdraw(17)
print("Child's account has ${}".format(childs_account.balance))
childs_account.accumulate_interest()
print("Child's account has ${}".format(childs_account.balance))

print()
print('----- OverdraftAccount:')
print()

overdraft_account = OverdraftAccount()
overdraft_account.deposit(12)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.withdraw(17)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.accumulate_interest()
print("Overdraft account has ${}".format(overdraft_account.balance))
