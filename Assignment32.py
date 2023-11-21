def is_armstrong_number(num):
    str_num = str(num)
    num_digits = len(str_num)
    armstrong_sum = sum(int(digit) ** num_digits for digit in str_num)
    return armstrong_sum == num
user_input = int(input("Enter a three-digit number: "))
result = is_armstrong_number(user_input)
if result:
    print(f"{user_input} is an Armstrong number.")
else:
    print(f"{user_input} is not an Armstrong number.")