heads = int(input("Enter the number of heads : "))
legs = int(input("Enter the number of legs : "))
C = (legs - 2 * heads) / 2
R = heads - C
if C >= 0 and R >= 0 and C.is_integer() and R.is_integer():
    print("Number of chickens : ", int(C))
    print("Number of rabbits : ", int(R))
else:
    print("No solution")