def is_perfect_number(num) :
    if num <= 1 :
        return False
    divisors_sum = 1
    for i in range(2, int(num ** 0.5) + 1) :
        if num % i == 0 :
            divisors_sum += i
            if i != num // i :
                divisors_sum += num // i
    return divisors_sum == num
def find_perfect_numbers(num_list) :
    perfect_numbers = [num for num in num_list if is_perfect_number(num)]
    return perfect_numbers
numbers_input = list(map(int, input("Enter a list of numbers separated by space : ").split()))
result = find_perfect_numbers(numbers_input)
if result :
    print("Perfect numbers in the list : ", result)
else :
    print("No perfect numbers found in the list.")