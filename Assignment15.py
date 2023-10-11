num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))
def is_valid_number(num) :
    return 10 <= num <= 99 and num % 5 == 0 and sum(map(int, str(num))) % 3 == 0
def find_maximum_number(num1, num2 ):
    max_number = -1
    valid_numbers = []
    if num1 >= num2 :
        return max_number
    for num in range(num1, num2 + 1) :
        if is_valid_number(num) :
            valid_numbers.append(num)
    if valid_numbers :
        max_number = max(valid_numbers)
    return max_number
result = find_maximum_number(num1, num2)
if result == -1 :
    print("No valid numbers found or invalid input.")
else :
    print("Maximum number : ", result)