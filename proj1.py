s = input("Enter the string Hello World : ")
ans = ""
if s[0] != "a" and s[0] != "e" and s[0] != "i" and s[0] != "o" and s[0] != "u" :
    ans+=s[0]
if s[1] != "a" and s[1] != "e" and s[1] != "i" and s[1] != "o" and s[1] != "u" :
    ans+=s[1]
if s[2] != "a" and s[2] != "e" and s[2] != "i" and s[2] != "o" and s[2] != "u" :
    ans+=s[2]
if s[3] != "a" and s[3] != "e" and s[3] != "i" and s[3] != "o" and s[3] != "u" :
    ans+=s[3]
if s[4] != "a" and s[4] != "e" and s[4] != "i" and s[4] != "o" and s[4] != "u" :
    ans+=s[4]
if s[5] != "a" and s[5] != "e" and s[5] != "i" and s[5] != "o" and s[5] != "u" :
    ans+=s[5]
if s[6] != "a" and s[6] != "e" and s[6] != "i" and s[6] != "o" and s[6] != "u" :
    ans+=s[6]
if s[7] != "a" and s[7] != "e" and s[7] != "i" and s[7] != "o" and s[7] != "u" :
    ans+=s[7]
if s[8] != "a" and s[8] != "e" and s[8] != "i" and s[8] != "o" and s[8] != "u" :
    ans+=s[8]
if s[9] != "a" and s[9] != "e" and s[9] != "i" and s[9] != "o" and s[9] != "u" :
    ans+=s[9]
print("New String = " , ans)

s = input("Enter hellowolrd : ")
a = ""
for x in s :
    if x != "a" and x != "e" and x != "i" and x != "o" and x != "u" :
        a+=x
print("Answer = " , a)

s = input("Enter hellowolrd : ")
a = ""
for x in s :
    if x not in "aeiouAEIOU":
        a+=x
print("Answer = " , a)

s = input("Enter helloworld : ")
a = "".join([x for x in s if x != "a" and x != "e" and x != "i" and x != "o" and x != "u"])
print(a)

s = input("Enter helloworld : ")
a = "".join([x for x in s if x not in "aeiouAEIOU"])
print(a)