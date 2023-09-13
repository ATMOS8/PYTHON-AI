s = int(input("Enter Current Salary : "))
l = int(input("Enter Job Level : "))
n = 0
if l == 3 :
    n = s + (15*s/100)
    print(f"New Salary = {n}")
elif l == 4 :
    n = s + (7*s/100)
    print(f"New Salary = {n}")
elif l == 5 :
    n = s + (5*s/100)
    print(f"New Salary = {n}")
else :
    print("Hike Package is 0")