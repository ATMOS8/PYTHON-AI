def calculate_profit(distance, passengers) :
    price_per_litre = 70
    mileage = 10
    price_per_ticket = 80
    fuel_cost = (distance / mileage) * price_per_litre
    revenue = passengers * price_per_ticket
    profit = revenue - fuel_cost
    if profit >= 0 :
        return profit
    else :
        return -1
distance = float(input("Enter the distance of the route (in km) : "))
passengers = int(input("Enter the number of passengers : "))
route_profit = calculate_profit(distance, passengers)
if route_profit == -1 :
    print("This route is running at a loss.")
else :
    print("Profit earned on this route : Rs", route_profit)