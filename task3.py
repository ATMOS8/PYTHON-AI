a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))
c = int(input("Enter Third Number : "))
p = 0
if a != 7 and b != 7 and c != 7 :
    p = a*b*c
    print(f"Product = {p}")
elif a == b :
    p = b*c
    print(f"Product = {p}")
elif b == 7 :
    p = c
    print(f"Product = {p}")
elif c == 7 :
    p = -1
    print(f"Product = {p}")