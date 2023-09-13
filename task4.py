o = int(input("Available 1 Rupees Coins : "))
f = int(input("Available 5 Rupees Coins : "))
a = int(input("Amount to be made : "))
fn = 0
on = 0
fn = a//5
on = a-(fn*5)
if fn <= f  and on <= o :
    print(f"No. of One Needed : {on}")
    print(f"No. of 5 Needed : {fn}")
elif (f - fn)*5 <= (o - on):
    on = on + ((fn - f)*5)
    fn = f
    if fn <= f and on <= o :
        print(f"No. of One Needed : {on}")
        print(f"No. of 5 Needed : {fn}")
    else :
        print("-1")
else :
    print("-1")