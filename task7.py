ft = input("Enter type of food : ")
q = int(input("Enter the quantity of plates ordered : "))
d = float(input("Enter the distance in kms from the Restaurant : "))
vc = 120
nc = 150
d3 = 0
d3_3 = 3
dr = 6
ba = 0
if (ft == 'V' or ft == 'N') and d >0 and q >= 1 :
    if ft == 'V' :
        ba = q*vc
    else :
        ba = q*nc

    if d <= 3 :
        ba += d*d3
    elif d <= 6 :
        ba += 3*d3+(d-3)*d3_3
    else :
        ba += 3*d3+3*d3_3+(d-6)*dr

    print(f"Final bill amount : Rs. {ba}")
else :
    print("Invalid input data. Bill amount : -1")