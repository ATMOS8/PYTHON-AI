r = float(input("Enter the amount needed in INR : "))
tc = input("Enter the traveller's Currency : ")
cr = {"Euro" : 0.01417, "Britsh Pound" : 0.0100, "Australian Dollar" : 0.02140, "Canadian Dollar" : 0.02027}
if tc in cr :
    atc = r/cr[tc]
    print(f"Amount to provide in {tc} : {atc}")
else :
    print("-1")