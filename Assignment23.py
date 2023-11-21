def create_largest_number(numbers):
    numbers = [str(num) for num in numbers]
    def custom_sort(a, b):
        return int(b + a) - int(a + b)
    numbers.sort(key=lambda x: x * 2, reverse=True)
    largest_number = ''.join(numbers)
    return int(largest_number)
input_numbers = input("Enter the list of two-digit numbers separated by commas:").split(',')
input_numbers = [int(num) for num in input_numbers]
result = create_largest_number(input_numbers)
print("The largest number possible by concatenating the list of numbers is:", result)