class Company:
    def addCompany(self, code, name, temp):
        self.code = code
        self.name = name
        self.temp = temp

    def show(self):
        print(f"{self.code} \t {self.name} \t {self.temp}")

c1 = Company()
c1.addCompany(1, "TCS", 6000)

c2 = Company()
c2.addCompany(2, "Infosys", 5000)

c3 = Company()
c3.addCompany(3, "L&T", 4000)

if c1.temp <= c2.temp <= c3.temp :
    c1.show()
elif c2.temp <= c1.temp <= c3.temp :
    c2.show()
elif c3.temp <= c1.temp <= c2.temp :
    c3.show()

c1.show()