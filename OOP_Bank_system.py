class BalanceException(Exception):
    pass

class BankAccount:
    def __init__ (self, initialAmt, AccName):
        self.balance = initialAmt
        self.name = AccName
        print(f"\nAccount '{self.name}' created. \nBalance = ${self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount '{self.name}'s Balance = {self.balance:.2f}")
        
    def deposit(self, amount):
        self.balance += amount 
        print("\nDepost Completed.")
        self.getBalance()

    def viableTrans(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"Sorry, Account '{self.name}' has only a balance of ${self.balance:.2f}")
        
    def withdraw(self, amount):
        try:
            self.viableTrans(amount)
            self.balance = self.balance - amount
            print("Withdraw Completed.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw Inturrupted {error}")

    def Transfer(self, amount, account):
        try:
            print("\n*********\n\nBeginning Transfer..🚀🚀🚀")
            self.viableTrans(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransfer Completed! ✅\n\n**********")
        except BalanceException as error:
            print(f"Transfer Inturrupted. ❌ {error} ")

class IntrestRewardAcc(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount *1.05)
        print("Deposit Completed.")
        self.getBalance()

class SavingsAcc(IntrestRewardAcc):
    def __init__ (self, initialAmount, accName):
        super().__init__(initialAmount, accName)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viableTrans(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("Withdraw Completed.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw Inturrupted: {error}")