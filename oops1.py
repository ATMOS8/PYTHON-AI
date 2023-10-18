class product:
    pass

p1 = product()
p1.prodid = 111
p1.prodname = "bottle"
p1.price = 30

p2 = product()
p2.prodid = 112
p2.prodname = "can"
p2.price = 60

print(p1.prodid, "\t", p1.prodname, "\t", p1.price)
print(p2.prodid, "\t", p2.prodname, "\t", p2.price)
