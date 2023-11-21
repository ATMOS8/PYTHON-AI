def check_anagram(str1, str2) :
    str1 = str1.lower()
    str2 = str2.lower()
    if len(str1) != len(str2):
        return False
    for char in str1 :
        if char.isdigit() or not char.isalnum() :
            continue
        if str1.count(char) != str2.count(char) :
            return False
    return True
string1 = input("Enter first string : ")
string2 = input("Enter second string : ")
result = check_anagram(string1, string2)
print(f"Are '{string1}' and '{string2}' anagrams? {result}")