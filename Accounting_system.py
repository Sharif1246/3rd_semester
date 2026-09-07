# week 3 2nd problem

from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self,account_number,owner,balance):
        self.account_number = account_number
        self.owner = owner
        self._balance = balance
    def deposit(self,amount):
        if amount > 0:
            self._balance += amount
        else:
            print("You have less money")

    def withdraw(self,amount):
        self._balance -= amount

    @abstractmethod
    def calculate_fee(self):
        pass

    @property
    def balance(self):
        return self._balance


class SavingsAccount(Account):
    def __init__(self,account_number,owner,balance, interest_rate):
        super().__init__(account_number,owner,balance)
        self.interest_rate = interest_rate

    def calculate_fee(self):
        return 0

class CurrentAccount(Account):
    def __init__(self,account_number,owner,balance, monthly_fee):
        super().__init__(account_number,owner,balance)
        self.monthly_fee = monthly_fee

    def calculate_fee(self):
        return self.monthly_fee

# savings = SavingsAccount("S001", "Ahmad", 1000, 0.05)
# current = CurrentAccount("C001", "Ali", 2000, 50)
#
# accounts = [savings,current]
#
# for account in accounts:
#     print(f"{account.owner}: Fee = {account.calculate_fee()}")
#
# print(savings.balance)

class Bank:
    def __init__(self):
        self.accounts = []
    def add_account(self,account):
        self.accounts.append(account)

savings = SavingsAccount("S001", "Ahmad", 1000, 0.05)
current = CurrentAccount("C001", "Ali", 2000, 50)

bank = Bank()

bank.add_account(savings)
bank.add_account(current)

for account in bank.accounts:
    print(f"{account.owner}: Fee = {account.calculate_fee()}")

