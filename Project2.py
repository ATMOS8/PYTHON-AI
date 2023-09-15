#Bank Transactions Project

import os

accounts = []

while True:
    print("1. Open Account")
    print("2. Show Account")
    print("3. Withdraw Amount")
    print("4. Deposit Amount")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        accno = int(input("Enter account number: "))
        accname = input("Enter account name: ")
        balance = float(input("Enter account opening balance: "))
        accounts.append({"accno": accno, "accname": accname, "balance": balance})
        print("Welcome to Mock Bank. Account created successfully")

    elif choice == 2:
        userinput = int(input("Enter account number: "))
        found = False
        for account in accounts:
            if account["accno"] == userinput:
                print("Account Details =", account["accno"], "\t", account["accname"], "\t", account["balance"])
                found = True
                break
        if not found:
            print("Invalid account number.")

    elif choice == 3:
        userinput = int(input("Enter account number: "))
        for account in accounts:
            if account["accno"] == userinput:
                withdraw_amount = float(input("Enter amount to be withdrawn: "))
                if withdraw_amount <= account["balance"]:
                    account["balance"] -= withdraw_amount
                    print("New balance:", account["balance"])
                else:
                    print("Insufficient Balance")
                break

    elif choice == 4:
        userinput = int(input("Enter account number: "))
        for account in accounts:
            if account["accno"] == userinput:
                deposit_amount = float(input("Enter the amount to be deposited: "))
                account["balance"] += deposit_amount
                print("New balance:", account["balance"])
                break

    elif choice == 5:
        break

    else:
        print("Invalid Choice")

        
with open("accounts.txt", "w") as file:
    for account in accounts:
        file.write(f"{account['accno']} {account['accname']} {account['balance']}\n")
