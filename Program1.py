from binascii import a2b_base64


account_number = int(input("Enter your Account Number : "))
x = str(account_number)
a1 = int(x[0])
a2 = int(x[1])
a3 = int(x[2])
a4 = int(x[3])
acc_no = ""
if a1 != 1 :
    print("Error!")
    exit()
account_balance = int(input("Enter your Account Balance : "))
if account_balance <= 100000 :
    print("Error!")
    exit()
salary = int(input("Enter your Salary : "))
loan_type = input("Enter the type of loan you want : ")
loan_amount_expected = int(input("Enter the expected loan amount : "))
customer_emi_expected = int(input("Enter the expected EMI : "))
if salary >= 25000 and loan_type == "Car" and loan_amount_expected <= 500000 and customer_emi_expected <= 36 :
    print(f"{account_number} is Eligible for this loan. \nRequested Loan Amount : {loan_amount_expected} \nEMI : {customer_emi_expected}")
elif salary >= 50000 and loan_type == "House" and loan_amount_expected <= 6000000 and customer_emi_expected <= 60 :
    print(f"{account_number} is Eligible for this loan. \nRequested Loan Amount : {loan_amount_expected} \nEMI : {customer_emi_expected}")
elif salary >= 75000 and loan_type == "Business" and loan_amount_expected <= 7500000 and customer_emi_expected <= 84 :
    print(f"{account_number} is Eligible for this loan. \nRequested Loan Amount : {loan_amount_expected} \nEMI : {customer_emi_expected}")
else :
    print("Error")