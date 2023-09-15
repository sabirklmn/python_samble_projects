#Bankin Application

account_No=0
CustName=" "
Bcode=" "
Mobile=0


def createAcounts():
    account_No=int(input("Enter acount Number: "))
    CustName=(input("Enter Name: "))
    Bcode=(input("Enter Branch code: "))
    Mobile=int(input("Enter Mobile number"))


def ShowaccountDetails():
    print("AcoountNO:",account_No)
    print("CustomerName:",CustName)
    print("Bcode:",Bcode)
    print("Mobile:",Mobile)


def Deposite(amount):

    Bal =Bal+amount
    checkbalance()


def Withdraw(amount):
    Bal=Bal - amount 
    checkbalance()


def checkbalance():
    print("current balanace:",Bal)


