#Bankin Application

account_No=0
CustName=" "
Bcode=" "
Mobile=0
Bal=0


def createAcounts():
    account_No=int(input("Enter acount Number: "))
    CustName=(input("Enter Name: "))
    Bcode=(input("Enter Branch code: "))
    Mobile=int(input("Enter Mobile number"))
    global Bal= int (input("enter current Balance"))

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

#Main driver code
ch1='y';
while (ch1=='y'):
    print("1.Create acount\n 2.Withdraw\n 3.deposit\n 4.checkbalance")
    ch=int(input("select any option"))


    if(ch==1):
        createAcounts()
    elif(ch==2):
        amnt=int(input("enter amount to withdraw"))
        Withdraw(amnt)
    elif(ch==3):
        amnt=int(input("enter ammount to deposite"))
        Deposite(amnt)
    elif(ch==4):
        checkbalance()
        
    else:
        print("please select any 4 options available above")
    print("do you want to continue... press y")
    ch1=input()




