def remove_duplicates(input_string) :
    unique_chars = []
    for char in input_string :
        if char not in unique_chars :
            unique_chars.append(char)
    return ''.join(unique_chars)
input_string = input("Enter a string : ")
result = remove_duplicates(input_string)
print("String after removing duplicates : ", result)