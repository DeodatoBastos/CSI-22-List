class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100


class Bus(Vehicle):
    def __init__(self, name, mileage, capacity, maintaince_fee):
        super().__init__(name, mileage, capacity)
        self.maintaince_fee = maintaince_fee

    def fare(self):
        return self.capacity * 100 * (1 + self.maintaince_fee)


School_bus = Bus("School Volvo", 12, 50, 0.1)
print("Total Bus fare is:", School_bus.fare())
