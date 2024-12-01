from OOP_Bank_system import *

Ali = BankAccount(3000, "Ali")
Bilal = BankAccount(5000, "Bilal")

Ali.getBalance()
Bilal.getBalance()

Ali.deposit(500)
Bilal.deposit(500)

Ali.withdraw(100)

Ali.Transfer(500, Bilal)

Junaid = IntrestRewardAcc(1000, "Junaid")

Junaid.getBalance()

Junaid.deposit(100)

Junaid.Transfer(100, Bilal)

Riz = SavingsAcc(2000, "Riz")

Riz.getBalance()

Riz.deposit(100)

Riz.Transfer(1000, Junaid)