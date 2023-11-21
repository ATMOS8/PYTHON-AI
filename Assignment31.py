def find_duplicates(numbers) :
    duplicates = []
    seen = set()
    for num in numbers :
        if num in seen and num not in duplicates :
            duplicates.append(num)
        else :
            seen.add(num)
    return duplicates
user_input = input("Enter a list of numbers separated by spaces : ")
input_list = list(map(int, user_input.split()))
result = find_duplicates(input_list)
print("The duplicate values in the list are : ", result)