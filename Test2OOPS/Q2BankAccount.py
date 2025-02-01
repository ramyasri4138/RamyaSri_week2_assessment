class BankAccount:
    def __init__(self,balance):
        self.balance=balance
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print("Amount deposited: ",amount)
            print("Balance after depositing: ",self.balance)
        else:
            print("Amount cannot be deposited")
    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient balance")
        else:
            self.balance-=amount
            print("amount withdrawn : ",amount)
            print("Remaining balance after withdrawal is ",self.balance)
            
b=BankAccount(100000)
b.deposit(1000)
b.withdraw(1000)
