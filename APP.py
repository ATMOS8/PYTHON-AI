menu_db = [
    {'code' : 'M801', 'itemname' : 'Sandwich', 'price' : 190, 'stock' : True},
    {'code' : 'M802', 'itemname' : 'Pizza', 'price' : 250, 'stock' : True},
    {'code' : 'M803', 'itemname' : 'Burger', 'price' : 160, 'stock' : True},
    {'code' : 'M804', 'itemname' : 'Colddrink', 'price' : 50, 'stock' : True},
    {'code' : 'M805', 'itemname' : 'Coffee', 'price' : 70, 'stock' : True},
    {'code' : 'M806', 'itemname' : 'Roll', 'price' : 120, 'stock' : True}
]
orders = []
inventory = {menu['itemname'] : {'qtys_sold' : 0, 'amount' : 0} for menu in menu_db}
def display_menus() :
    print("Available Menus:")
    for menu in menu_db :
        if menu['stock'] :
            print(f"{menu['code']}    {menu['itemname']}    {menu['price']}")
def add_to_order(order_str) :
    order_items = order_str
    order_data = {'menus' : []}
    for item in order_items :
        item_code, qty = item
        menu = next((m for m in menu_db if m['code'] == item_code))
        if menu :
            order_data['menus'].append({
                'code' : item_code,
                'itemname' : menu['itemname'],
                'price' : menu['price'],
                'stock' : menu['stock'],
                'qtys' : int(qty)
            })
            print(f"Menu '{item_code}' created order successfully")
            inventory[menu['itemname']]['qtys_sold'] += int(qty)
            inventory[menu['itemname']]['amount'] += menu['price'] * int(qty)
        else :
            print(f"Menu '{item_code}' does not exist. Try again.")
    orders.append(order_data)
def display_orders() :
    for order_num, order in orders :
        print(f"#Order number: {order_num}")
        print("Code    Item Name    Price    Quantity    Total")
        total_order_amount = 0
        for menu in order['menus'] :
            print(f"{menu['code']}    {menu['itemname']}    {menu['price']}    {menu['qtys']}    {menu['price'] * menu['qtys']}")
            total_order_amount += menu['price'] * menu['qtys']
        print("---------------------------------------------")
        print(f"Total : {total_order_amount}\n")
def display_inventory() :
    print("Menu Name           Issued Qtys          Amount")
    total_profit = 0
    for itemname, data in inventory.items() :
        print(f"{itemname}          {data['qtys_sold']}          {data['amount']}")
        total_profit += data['amount']
    print(f"\nTotal Amount in Profit is {total_profit}")
while True :
    print("\nOptions :")
    print("1. Display Menus")
    print("2. Add to Order")
    print("3. Display Orders")
    print("4. Display Inventory")
    print("5. Exit")
    choice = input("Enter your choice : ")
    if choice == '1' :
        display_menus()
    elif choice == '2' :
        order_str = input("Enter your order (e.g.,M801 3) : ")
        add_to_order(order_str)
    elif choice == '3' :
        display_orders()
    elif choice == '4' :
        display_inventory()
    elif choice == '5' :
        break
    else :
        print("Invalid choice. Please try again.")