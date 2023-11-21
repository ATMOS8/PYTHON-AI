def find_ten_substring(num_str) :
    ten_substrings = []
    try :
        for i in range(len(num_str)) :
            for j in range(i + 1, len(num_str) + 1) :
                substring = num_str[i : j]
                if sum(int(digit) for digit in substring) == 10 :
                    ten_substrings.append(substring)
        return ten_substrings
    except Exception as e :
        print(f"Error : {e}")
        return []
user_input = input("Enter a string of digits : ")
result = find_ten_substring(user_input)
print("The 10-substrings are :", result)