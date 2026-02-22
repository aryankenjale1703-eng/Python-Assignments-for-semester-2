class BankAccount:
    def __init__(self,acc_no,bal):
        self.acc_no = acc_no
        self.balance = bal
    def deposite(self):
        amt = float(input("Enter amount to deposite: "))
        self.balance = self.balance + amt
        print("deposite",amt)

    def withdraw(self):
        amt = float(input("Enter amount to withdraw: "))
        if amt<= self.balance:
            self.balance = self.balance - amt
            print("Withdraw",amt)

        else:
            print("Not enough balance")

    def check_balance(self):
        print("current balance",self.balance)
acc = input("Enter account number: ")
bal = float(input("Enter initial balance: "))
obj = BankAccount(acc,bal)
while True:
    print("\n1 deposite")
    print("2 withdraw")
    print("3 check balance")
    print("4 exist")

    ch = input("enter choice: ")

    if ch == "1":
        obj.deposite()
    elif ch =="2":
        obj.withdraw()
    elif ch == "3":
        obj.check_balance()
    elif ch =="4":
        print("Thank you")
        break
    else:
        print("Wrong choice")
     