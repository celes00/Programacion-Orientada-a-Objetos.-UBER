from car import Car

class UberVan(Car):
    typeCarAccepted = []
    seatsMaterial = []
    
    def __init__(self, license, driver, typeCarAccepted, seatsMAterial):
        super().__init__(license, driver)
        self.typeCarAccepted = typeCarAccepted
        self.seatsMaterial = seatsMAterial
    