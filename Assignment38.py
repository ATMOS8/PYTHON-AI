def odd(sample_data) :
    return [num for num in sample_data if num % 2 != 0]
def even(sample_data) :
    return [num for num in sample_data if num % 2 == 0]
def sum_of_numbers(sample_data, func=None) :
    if func is None :
        return sum(sample_data)
    else :
        return sum(func(sample_data))
sample_data = range(1, 11)
user_input = input("Enter 'even' or 'odd' to get sum of even or odd numbers : ")
if user_input == 'even' :
    result = sum_of_numbers(sample_data, even)
    print("Sum of even numbers:", result)
elif user_input == 'odd' :
    result = sum_of_numbers(sample_data, odd)
    print("Sum of odd numbers :", result)
else :
    result = sum_of_numbers(sample_data)
    print("Sum of all numbers :", result)