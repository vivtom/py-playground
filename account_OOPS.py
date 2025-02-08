class Account():
    def __init__(self,balance,account_number):
        self.balance = balance
        self.account_number = account_number
    def print_balance(self):
        print(self.balance)
    def credit(self,amount):
        self.balance += amount 
    def debit(self,amount):
        self.balance -= amount
    
acc1 = Account(3000,2)
acc1.debit(2000)
acc1.credit(3000)
acc1.print_balance()
    


