class atm():
    name = input("Write your name here :- ")
    mobno = input("Write your Mobile name here :- ")
    atm = input("Write your atm card number here :- ")
    pin = input("Write your pin number here :- ")
    cash = input("Write your cash widrawel here :- ")
    
    def Atm(self,name,mobno,atm,pin,cash):
        self.name = name
        self.mobno = mobno
        self.atm = atm
        self.pin = pin
        self.cash = cash

    print("Your informations are ready :- ")
    print("Name :- ", name)
    print("Mobile No. :- ", mobno)
    print("Atm Card No. :- ", atm)
    print("Pin No. :- ", pin)
    print("Cah Widrawel :- ", cash)
    