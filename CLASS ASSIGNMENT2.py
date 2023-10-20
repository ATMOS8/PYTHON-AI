class Flight :
    def addFlight(self, flightcode, flightname, airportname, fuelcap, passangers_count) :
        self.flightcode = flightcode
        self.flightname = flightname
        self.airportname = airportname
        self.fuelcap = fuelcap
        self.passangers_count = passangers_count
    def show(self):
        print(f" Flight Code : {self.flightcode} \n Flight Name : {self.flightname} \n Airport Name : {self.airportname} \n Fuel Capacity : {self.fuelcap} Litres \n Passengers Count : {self.passangers_count} \n\n")
f1 = Flight()
f1.addFlight("F001", "Flight A", "Airport X", 10000, 150)
f2 = Flight()
f2.addFlight("F002", "Flight B", "Airport Y", 15000, 160)
f3 = Flight()
f3.addFlight("F003", "Flight C", "Airport Z", 20000, 170)
FlightList = [f1, f2, f3]
for item in FlightList :
    item.show()