def is_palindrome(num):
    return str(num) == str(num)[::-1]
def nearest_palindrome(number):
    number += 1
    while True:
        if is_palindrome(number):
            return number
        number += 1
user_input = int(input("Enter a number: "))
result = nearest_palindrome(user_input)
print(f"The nearest palindrome greater than {user_input} is:", result)