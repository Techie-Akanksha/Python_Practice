# OOPS CONCEPT

class BankAccount:
    def __init__(self,owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposit successful")
        else:
            print("Invalid amount")

    def withdraw(self,amount):
        if self.balance >= amount and amount > 0:
            self.balance -= amount
            print("Withdraw successful")
        else:
            print("Insufficient Balance")
        
    def show_balance(self):
        return self.balance

account1 = BankAccount("Rahul", 1000)
balance = account1.show_balance()
account1.deposit(500)
account1.withdraw(-1500)
print(balance)