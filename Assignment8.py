account_number = input("Enter your 4-digit account number: ")
account_balance = float(input("Enter your account balance in Rupees: "))
salary = float(input("Enter your salary in Rupees: "))
loan_type = input("Enter the loan type (Car, House, Business): ").lower()
loan_amount_expected = float(input("Enter the loan amount you expect in Rupees: "))
customer_emi_expected = int(input("Enter the number of EMI's you expect: "))
def is_valid_account_number(account_number):
    return len(account_number) == 4 and account_number[0] == '1' and account_number.isdigit()
def calculate_loan_emi(salary, loan_type):
    eligible_loan_amount = 0
    emi_count = 0
    if salary > 25000:
        if loan_type == "car":
            eligible_loan_amount = 500000
            emi_count = 36
        elif loan_type == "house":
            eligible_loan_amount = 6000000
            emi_count = 60
        elif loan_type == "business":
            eligible_loan_amount = 7500000
            emi_count = 84
    return eligible_loan_amount, emi_count
if is_valid_account_number(account_number) and account_balance >= 100000:
    eligible_loan_amount, emi_count = calculate_loan_emi(salary, loan_type)
    if loan_amount_expected <= eligible_loan_amount and customer_emi_expected <= emi_count:
        print("Account Number:", account_number)
        print("Eligible Loan Amount:", eligible_loan_amount, "Rupees")
        print("Requested Loan Amount:", loan_amount_expected, "Rupees")
        print("Number of EMI's Required to Repay:", customer_emi_expected)
    else:
        print("Error: Requested loan amount or EMI's are not within the bank's limits.")
else:
    print("Error: Invalid account number or insufficient balance in the account.")