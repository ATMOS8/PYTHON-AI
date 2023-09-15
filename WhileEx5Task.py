'''
Q1. print following pattern for n times
when n=5
1 2 3 4 5
5 4 3 2 1
1 2 3 4 5
5 4 3 2 1
1 2 3 4 5
'''
n = int(input("Enter value of n: "))
r = 1
while r <= n:
    c = 1
    while c <= n:
        if r % 2 == 1:
            print(c, end=" ")
        else:
            print(n - c + 1, end=" ")
        c += 1
    print()
    r += 1

'''
Q2. print following pattern for n times
when n=5
11 12 13 14 15
11 12 13 14
11 12 13
11 12 
11
'''
n = int(input("Enter value of n: "))
r = n
while r >= 1:
    c = 1
    while c <= r:
        print(10 + c, end=" ")
        c += 1
    print()
    r -= 1

'''
Q3. print following pattern for n times
when n=5
A B C D E
a b c d e
A B C D E
a b c d e 
A B C D E
'''
n = int(input("Enter value of n: "))
r = 1
while r <= n:
    c = 1
    while c <= n:
        if r % 2 == 1:
            print(chr(64 + c), end=" ")
        else:
            print(chr(96 + c), end=" ")
        c += 1
    print()
    r += 1