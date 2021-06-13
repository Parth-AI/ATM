class ATM:
     def __init__(self, carNumber, cashToWithdraw = 0, ammountLeft = 1000000):
          self.cashToWithdraw = cashToWithdraw
          self.carNumber = carNumber
          self.ammountLeft = ammountLeft-cashToWithdraw
     
     def WithDrawCash(self):
          print(f"Your card number is {self.carNumber} cash withdrawn is {self.cashToWithdraw} and amount left is {self.ammountLeft}")

     def BalanceLeft(self):
          print(f"Your card number is {self.carNumber} and amount left is {self.ammountLeft}")

a = input("Enter what you want to do:-\n\tWithDrawCash\n\tAmountleft\n\n ")
if a == "WithDrawCash":
     cwd = int(input("Enter the amount you want to withdraw:- "))
     Money = ATM(123456789, cwd)
     Money.WithDrawCash()
elif a == "Amountleft":
     Money = ATM(123456789)
     Money.BalanceLeft()
