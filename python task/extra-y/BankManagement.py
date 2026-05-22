"""Create a Bank Account Management Program that includes the following methods:
Add balance amount (Deposit money by the account holder).
Show balance.
Withdraw balance (Minimum balance should be 100).
Balance cannot be accessed directly from outside the class."""

class BankAccount():
    def __init__(self, balance):
        self.__bankBalance = balance
        
    def deposit(self ,addMoney):
        self.addMoney = addMoney
        self.__bankBalance += addMoney
        print("Amount Deposit :",self.addMoney)
        bankAccount.checkBalance()
        
        
    def checkBalance(self):
        print("Current balacne :",self.__bankBalance)

    def withdraw(self ,withdrawBalance):
        self.withdrawBalance = withdrawBalance
        if self.withdrawBalance < self.__bankBalance:
            if self.withdrawBalance < 100 :
                print("Withbraw account must be ABOVE 100.")
                return
            else:
                self.__bankBalance -= self.withdrawBalance
                print("Withbraw Amount :",self.withdrawBalance)
                bankAccount.checkBalance()
        else:
            #print("Low Balance")
            print("Transcation Failed due to Low Balacne")
        
bankAccount = BankAccount(500)

while(1):
    try:
        print("=================================")
        print("1.Check Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("*Press CTRL+C for exit")
        n = int(input("Enter Choice : "))
        if(n==1):
            bankAccount.checkBalance()
            exit

        elif(n==2):
            try:
                d=float(input("Enter number for Deposit : "))
                bankAccount.deposit(d)
            except ValueError:
                print("Enter only number.")
            exit
                        
        elif(n==3):
            try:
                w = float(input("Enter number for withdraw : "))
                bankAccount.withdraw(w)
            except ValueError:
                print("Enter onl")
                exit
                        
        else:
            print("Enter given option")
            
    except ValueError:
        print("Enter number only.")
    