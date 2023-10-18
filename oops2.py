class product:

    def np(self):
        self.prodid = int(input("Enter product id : "))
        self.name = input("Enter product name : ")
        self.price = int(input("Enter product price : "))

    def show(self):
        print(f"{self.prodid}")
        print(f"{self.name}")
        print(f"{self.price}")

p1 = product()
p1.np()

p2 = product()
p2.np()

p3 = product()
p3.np()

p1.show()
p2.show()
p3.show()