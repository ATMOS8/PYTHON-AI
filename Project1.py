#Bank Transactions Project

import os

accno = acname = balance = None

while True:
    
    print("1. Open Account")
    print("2. Show Account")
    print("3. Withdraw Amount")
    print("4. Deposit Amount")
    print("5. Exit")

    choice = int(input("Enter choice :"))
    os.system("cls")

    if choice==1:
        accno = int(input("Enter account number :"))    
        accname = input("Enter account name :")
        balance = float(input("Enter account opening balance :"))
        print("Welcome to Mock Bank. Account created successfully")

    elif choice==2:
        userinput = int(input("Enter account number :"))
        if userinput == accno:
            print("Account Details = ", accno, "\t", accname, "\t", balance)
        else:
            print("Invalid account number.")
            
    elif choice==3:
        userinput = int(input("Enter account number :"))
        if userinput == accno:
            withdraw_amount = float(input("Enter amount to be withdrawn : "))
            if withdraw_amount <= balance :
                balance = balance - withdraw_amount
                print(balance)
            else : 
                print("Insufficient Balance")
    elif choice==4:
        userinput = int(input("Enter account number :"))
        if userinput == accno:
            deposite_amount = int(input("Enter the amount to be deposited : "))
            balance = balance + deposite_amount
            print(balance)
        
    elif choice==5:
        os.system("exit")
    else:
        print("Invalid Choice")