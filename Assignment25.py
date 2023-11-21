def check_double(number):
    str_num = str(number)
    str_double = str(number * 2)
    if len(str_num) != len(str_double):
        return False
    for digit in str_num:
        if digit not in str_double or str_num.count(digit) != str_double.count(digit):
            return False
    return True
user_input = int(input("Enter a whole number: "))
result = check_double(user_input)

if result:
    print(f"The number {user_input} satisfies the given conditions.")
else:
    print(f"The number {user_input} does not satisfy the given conditions.")