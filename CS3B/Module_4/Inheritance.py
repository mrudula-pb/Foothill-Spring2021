class Vehicle:
    def __init__(self):
        self._headlight_status = False  # headlight off to save battery

    @property
    def headlight_status(self):
        return self._headlight_status

    @headlight_status.setter
    def headlight_status(self, state: bool):  # expecting boolean for status
        self._headlight_status = state


class GasVehicle(Vehicle):
    def __init__(self):
        self._tank_status = "Empty"
        super().__init__()

    # it's an instance method
    def fuel_up(self):
        print("Going to the gas station")
        self._tank_status = "Full"


class ElectricVehicle(Vehicle):
    def __init__(self):
        self._battery_status = "Empty"
        super().__init__()

    def fuel_up(self):  # This method is static because it's not altering any instance variables
        print('Charging Now!')
        self._battery_status = "Full"


# rusty_vehicle = Vehicle()
# rusty_vehicle.headlight_status = True
#
# if rusty_vehicle.headlight_status:
#     print("Headlights ON")
# else:
#     print("Headlights OFF")


rusty_gas = GasVehicle()

if rusty_gas._headlight_status:
    print("Headlight ON")
else:
    print('Headlight OFF')

rusty = ElectricVehicle()

# rusty.headlight_status = True

if rusty._headlight_status:
    print("Headlight ON")
else:
    print('Headlight OFF')

rusty.fuel_up()
# rusty_gas.fuel_up()
