m = int(input("Mileage of the vehicle : "))
a = int(input("Amount per litre of fuel : "))
d = int(input("Distance for one way : "))
e = (2*d*a/m)/4
print(f"Amount paid by each one is {e} Rupees.")
if e % 5 == 0 :
    print("True")
else :
    print("False")