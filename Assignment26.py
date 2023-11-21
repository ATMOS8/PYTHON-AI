class FoodVendor:
    def __init__(self, menu, quantities):
        self.menu = menu
        self.quantities = quantities
    def place_order(self, orders):
        for item, quantity in orders:
            if item not in self.menu:
                print(f"{item} is not available")
            else:
                idx = self.menu.index(item)
                available = self.check_quantity_available(idx, quantity)
                if available:
                    print(f"{item} is available")
                else:
                    print(f"{item} stock is over")
    def check_quantity_available(self, index, quantity_requested):
        if self.quantities[index] >= quantity_requested:
            self.quantities[index] -= quantity_requested
            return True
        return False
menu_items = ["Veg Roll", "Noodles", "Fried Rice", "Soup"]
quantities_available = []
for item in menu_items:
    quantity = int(input(f"Enter quantity available for {item}: "))
    quantities_available.append(quantity)
vendor = FoodVendor(menu_items, quantities_available)
orders_input = input("Enter items ordered with quantities (item1,quantity1 item2,quantity2 ...): ")
orders_list = orders_input.split()
orders = []
for order in orders_list:
    item, quantity = order.split(',')
    orders.append((item.strip(), int(quantity)))
vendor.place_order(orders)