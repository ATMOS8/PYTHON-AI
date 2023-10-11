def find_common_characters(str1, str2) :
    set1 = set(str1.replace(" ", ""))
    set2 = set(str2.replace(" ", ""))
    common_characters = set1.intersection(set2)
    common_characters = ''.join(sorted(common_characters))
    if common_characters :
        return common_characters
    else :
        return -1
string1 = input("Enter the first string : ")
string2 = input("Enter the second string : ")
result = find_common_characters(string1, string2)
if result == -1 :
    print("No common characters found.")
else :
    print("Common characters : ", result)