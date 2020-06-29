class Car:
    def __init__(self, name, steering, brakes):
        self.name = name
        self.steering = steering
        self.brakes = brakes

    def fuelTank(self):
        print("To fill the tank, open tank's lid and fill fuel! ")

    def show(self):
        print("The car's name is", self.name)
        self.fuelTank()
        print("The car's steering is", self.steering)
        print("The car's brakes are", self.brakes)


x = Car("Maruti", "Manual Steering", "Hydraulic Breaks")
y = Car("Santro", "Power Steering", "Gas Breaks")

x.show()
y.show()






