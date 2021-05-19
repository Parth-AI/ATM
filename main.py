class ATM:
     def __init__(self, cashToWithdraw, carNumber, ammountLeft = 1000000):
          self.cashToWithdraw = cashToWithdraw
          self.carNumber = carNumber
          self.ammountLeft = ammountLeft-cashToWithdraw
     
     def money(self):
          print(f"Your card number is {self.carNumber} cash withdrawn is {self.cashToWithdraw} and amount left is {self.ammountLeft}")

Money = ATM(100000, 123456789)
Money.money()
