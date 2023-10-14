def find_pairs_of_numbers() :
    numbers = input("Enter a list of positive integers separated by spaces : ")
    numbers = [int(num) for num in numbers.split()]
    n = int(input("Enter the target sum (n) : "))
    count = 0
    seen = set()
    for num in numbers :
        complement = n - num
        if complement in seen :
            count += 1
        seen.add(num)
    return count
result = find_pairs_of_numbers()
print(f"Number of pairs that add up to n: {result}")