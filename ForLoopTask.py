
#Q1. Ask user to input n1 and n2. print even numbers between them using for loopn1 = int(input("Enter first number : "))
n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
if n1 > n2 :
    n1, n2 = n2, n1
for n in range(n1, n2 + 1) :
    if n % 2 == 0 :
        print(n)

#Q2. Ask user to input any number and print its factorial
n = int(input("Enter a number: "))
f = 1
if n < 0:
    print("No Factorial for Negative Numbers")
elif n == 0:
    print(1)
else:
    for i in range(1, n + 1):
        f *= i
    print(f)

#Q3. Print prime numbers between 1 to 100 using for loop
def p(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
print("Prime numbers between 1 and 100:")
for i in range(1, 101):
    if p(i):
        print(i, end=" ")

#Q4. WAP to input value of n and print fibonancii series
#   0, 1, 1, 2, 3, 5, 8, 13, 21,   so on   upto n
n = int(input("Enter the value of n: "))
fa, fb = 0, 1
print("Fibonacci series up to", n, "terms:")
print(fa, end=", ")
print(fb, end=", ")
for _ in range(2, n):
    fnext = fa + fb
    print(fnext, end=", ")
    fa, fb = fb, fnext
print()