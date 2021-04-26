
class Car:
    """A simple attempt to model a car."""

    def __init__(self, make, model, year):
        """Initialize car attributes."""
        self.make = make
        self.model = model
        self.year = year
        self.fuel_tank = FuelTank()

    def get_descriptive_name(self):
        """Print a neatly formatted description of the car."""
        long_name = f"{self.year} {self.make} {self.model}"
        print(long_name.title())

    def drive(self):
        """Simulate driving."""
        print("The car is moving.")


class FuelTank():
    """A simple attempt to model a vehicle's fuel tank."""

    def __init__(self):
        """Initialize the fuel tank's attributes."""
        self.fuel_capacity = 12
        self.fuel_level = 0

    def fill_tank(self):
        """Fill gas tank to capacity."""
        self.fuel_level = 12
        print(f"Your tank is now full with {self.fuel_capacity} gallons of fuel.")

    def add_fuel(self, amount):
        """Add fuel to the tank."""
        if self.fuel_level + amount < self.fuel_capacity:
            self.fuel_level += amount
            print(f"Added {amount} gallons of fuel to your tank.")
            print(f"You can still add {self.fuel_capacity - self.fuel_level} gallon(s) of fuel to your tank.")
        elif self.fuel_level + amount > self.fuel_capacity:
            print(f"You tried to add {amount} gallons of fuel to your tank, but your tank can only hold {self.fuel_capacity - self.fuel_level} gallons. Please, add only {self.fuel_capacity - self.fuel_level} gallons.")
        elif self.fuel_level + amount == self.fuel_capacity:
            self.fuel_level += amount
            print(f"You added {amount} gallons of fuel to your tank.")
            print("Your tank is full.")        
        
    def update_fuel_level(self, new_level):
        """Update the fuel level."""
        if new_level <= self.fuel_capacity:
            self.fuel_level = new_level
            print(f"You have {new_level} gallon(s) of fuel left in your tank.")
        else:
            print("The tank won't hold that much.")


class ElectricCar(Car):
    """A simple model of an electric car."""

    def __init__(self, make, model, year):
        """Initialize an elctric car."""
        super().__init__(make, model, year)
        # Attributes specific to electric cars.
        # Battery capacity in kWh
        self.battery_size = 85
        # Charge level in percent
        self.charge_level = 0
        self.battery = Battery()

    def fill_tank(self):
        """Display an error message."""
        print("This car has no fuel tank.")

    def charge(self):
        """Fully charge the vehicle."""
        self.battery.charge_level = 100
        print("Your vehicle is fully charged.")


class Battery:
    """A battery for an electric car."""

    def __init__(self, size=85):
        """Initialize battery attributes."""
        # Capacity in kWh, charge level in %
        self.size = size
        self.charge_level = 0

    def get_range(self):
        """Return the battery's range."""
        if self.size == 85:
            return 390
        elif self.size == 100:
            return 415


my_car = Car('hyundai', 'elantra', 2012)
my_car.get_descriptive_name()
my_car.fuel_tank.add_fuel(11)
my_car.fuel_tank.add_fuel(1)

my_ecar = ElectricCar('tesla', 'model s', 2021)
my_ecar.get_descriptive_name()
my_ecar.charge()
print(my_ecar.battery.get_range())
my_ecar.drive()
