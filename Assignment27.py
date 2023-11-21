def is_palindrome(s):
    s = s.lower()
    if len(s) <= 1:
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False
user_input = input("Enter a string: ")
result = is_palindrome(user_input)
if result:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")