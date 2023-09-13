gems = {"Ruby" : 2500, "Saphire" : 3000, "Emrald" : 1500, "Diamond" : 5000, "Pearl" : 1000}
total_bill = 0
discount_percentage = 0
while True :
    gem_name = input("Enter the name of the gem : ")
    if gem_name == 'done' :
        break
    if gem_name in gems :
        quantity = int(input(f"Enter the quantity of {gem_name} : "))
        if quantity > 0 :
            total_bill += gems[gem_name]*quantity 
        else :
            print("Quantity must be greater than than 0.")
    else :
        print("Gem not available in the store.")
        total_bill = -1
        break
if total_bill > 30000:
    discount_percentage = 5
    discount_amount = (total_bill*discount_percentage)/100
    total_bill -= discount_amount
if total_bill != -1:
    print(f"Total bill amount: Rs. {total_bill}")
else:
    print("Sorry, we couldn't process your order.")