"""A class that can be used to represent a car."""

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 23
        self.fuel_tank = FuelTank()
        self.drive_range = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title() 

    def drive(self, miles):
        """Represent driving the car."""
        self.drive_range = miles
        if self.fuel_tank.fuel_level <= 0:
            print("You have run out of gas! You must add fuel to your fuel tank to continue driving.")
        elif self.drive_range >= 30 and self.drive_range < 60:
            self.fuel_tank.fuel_level -= 1
            print("The car is moving.")
            print(f"You drove your car for {miles} miles.")
            self.odometer_reading += miles
            print(f"You have {self.fuel_tank.fuel_level} gallons of fuel left in your tank")
        elif self.drive_range >= 60 and self.drive_range < 90:
            self.fuel_tank.fuel_level -= 2
            print("The car is moving.")
            print(f"You drove your car for {miles} miles.")
            self.odometer_reading += miles
            print(f"You have {self.fuel_tank.fuel_level} gallons of fuel left in your tank")
        elif self.drive_range >= 90 and self.drive_range < 120:
            self.fuel_tank.fuel_level -= 3
            print("The car is moving.")
            print(f"You drove your car for {miles} miles.")
            self.odometer_reading += miles
            print(f"You have {self.fuel_tank.fuel_level} gallons of fuel left in your tank")
        elif self.drive_range >= 120 and self.drive_range < 150:
            self.fuel_tank.fuel_level -= 4
            print("The car is moving.")
            print(f"You drove your car for {miles} miles.")
            self.odometer_reading += miles
            print(f"You have {self.fuel_tank.fuel_level} gallons of fuel left in your tank")
        elif self.drive_range >= 150 and self.drive_range < 180:
            self.fuel_tank.fuel_level -= 5
            print("The car is moving.")
            print(f"You drove your car for {miles} miles.")
            self.odometer_reading += miles
            print(f"You have {self.fuel_tank.fuel_level} gallons of fuel left in your tank")
        elif self.drive_range >= 180 and self.drive_range < 210:
            self.fuel_tank.fuel_level -= 6
            print("The car is moving.")
            print(f"You drove your car for {miles} miles.")
            self.odometer_reading += miles
            print(f"You have {self.fuel_tank.fuel_level} gallons of fuel left in your tank")
        elif self.drive_range >= 210 and self.drive_range < 240:
            self.fuel_tank.fuel_level -= 7
            print("The car is moving.")
            print(f"You drove your car for {miles} miles.")
            self.odometer_reading += miles
            print(f"You have {self.fuel_tank.fuel_level} gallons of fuel left in your tank")
        elif self.drive_range >= 240 and self.drive_range < 270:
            self.fuel_tank.fuel_level -= 8
            print("The car is moving.")
            print(f"You drove your car for {miles} miles.")
            self.odometer_reading += miles
            print(f"You have {self.fuel_tank.fuel_level} gallons of fuel left in your tank")
        elif self.drive_range >= 270 and self.drive_range < 300:
            self.fuel_tank.fuel_level -= 9
            print("The car is moving.")
            print(f"You drove your car for {miles} miles.")
            self.odometer_reading += miles
            print(f"You have {self.fuel_tank.fuel_level} gallons of fuel left in your tank")
        elif self.drive_range >= 300 and self.drive_range < 330:
            self.fuel_tank.fuel_level -= 10
            print("The car is moving.")
            print(f"You drove your car for {miles} miles.")
            self.odometer_reading += miles
            print(f"You have {self.fuel_tank.fuel_level} gallons of fuel left in your tank")
        elif self.drive_range >= 330 and self.drive_range < 360:
            self.fuel_tank.fuel_level -= 11
            print("The car is moving.")
            print(f"You drove your car for {miles} miles.")
            self.odometer_reading += miles
            print(f"You have {self.fuel_tank.fuel_level} gallons of fuel left in your tank")
        elif self.drive_range >= 360 and self.drive_range < 370:
            self.fuel_tank.fuel_level -= 11.333
            print("The car is moving.")
            print(f"You drove your car for {miles} miles.")
            self.odometer_reading += miles
            print(f"You have {self.fuel_tank.fuel_level} gallons of fuel left in your tank")
        elif self.drive_range >= 370 and self.drive_range < 390:
            self.fuel_tank.fuel_level -= 12
            print("The car is moving.")
            print(f"You drove your car for {miles} miles.")
            self.odometer_reading += miles
            print(f"Warning!!!! You are almost out of fuel! Add fuel now!")
        elif self.drive_range > 390:
            print("The car is moving.")
            print(f"You drove your car for 390 miles and ran out of gas!")
            self.fuel_tank.fuel_level -= 12
            self.odometer_reading += 390
        elif self.fuel_tank.fuel_level <= 0:
            print("You have run out of gas!")

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    

class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
        self.charge_level = 0

    def charge(self):
        """Fully charge the battery."""
        self.charge_level = 100
        print("The vehicle is fully charged.")

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
            
        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        """Upgrade the battery from size=75 to size=100"""
        if self.battery_size == 75:
            self.battery_size = 100
        elif self.battery_size == 100:
            return self.battery_size


class FuelTank():
    """A simple attempt to model a vehicle's fuel tank."""

    def __init__(self):
        """Initialize the fuel tank's attributes."""
        self.fuel_capacity = 12
        self.fuel_level = 0

    def read_fuel_level(self):
        """Read the fuel level."""
        if self.fuel_level <= 0:
            print("Your fuel tank is empty.")
        elif self.fuel_level == 1:
            print(f"You have {self.fuel_level} gallons left in your tank.")
        elif self.fuel_level == 2:
            print(f"You have {self.fuel_level} gallons left in your tank.")
        elif self.fuel_level == 3:
            print(f"You have {self.fuel_level} gallons left in your tank.")
        elif self.fuel_level == 4:
            print(f"You have {self.fuel_level} gallons left in your tank.")
        elif self.fuel_level == 5:
            print(f"You have {self.fuel_level} gallons left in your tank.")
        elif self.fuel_level == 6:
            print(f"You have {self.fuel_level} gallons left in your tank.")
        elif self.fuel_level == 7:
            print(f"You have {self.fuel_level} gallons left in your tank.")
        elif self.fuel_level == 8:
            print(f"You have {self.fuel_level} gallons left in your tank.")
        elif self.fuel_level == 9:
            print(f"You have {self.fuel_level} gallons left in your tank.")
        elif self.fuel_level == 10:
            print(f"You have {self.fuel_level} gallons left in your tank.")
        elif self.fuel_level == 11:
            print(f"You have {self.fuel_level} gallons left in your tank.")
        elif self.fuel_level == 12:
            print(f"You have {self.fuel_level} gallons left in your tank.")
        elif self.fuel_level == 13:
            print(f"You have {self.fuel_level} gallons left in your tank.")
        elif self.fuel_level == 14:
            print(f"You have {self.fuel_level} gallons left in your tank.")
        elif self.fuel_level == 15:
            print(f"You have {self.fuel_level} gallons left in your tank.")
        elif self.fuel_level == 16:
            print(f"You have {self.fuel_level} gallons left in your tank.")
        elif self.fuel_level == 17:
            print(f"You have {self.fuel_level} gallons left in your tank.")
        elif self.fuel_level == 18:
            print(f"You have {self.fuel_level} gallons left in your tank.")
        elif self.fuel_level == 19:
            print(f"You have {self.fuel_level} gallons left in your tank.")
        elif self.fuel_level == 20:
            print(f"You have {self.fuel_level} gallons left in your tank.")
        elif self.fuel_level == 21:
            print(f"You have {self.fuel_level} gallons left in your tank.")
        elif self.fuel_level == 22:
            print(f"You have {self.fuel_level} gallons left in your tank.")
        elif self.fuel_level == 23:
            print(f"You have {self.fuel_level} gallons left in your tank.")
        elif self.fuel_level == 24:
            print(f"You have {self.fuel_level} gallons left in your tank.")
        elif self.fuel_level == 25:
            print(f"You have {self.fuel_level} gallons left in your tank.")

    def tank_size(self, fuel_capacity):
        """Define the size of the fuel tank."""
        self.fuel_capacity = fuel_capacity

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
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the Parent Class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()


my_car = Car('hyundai', 'elantra', 2012)
print(f"\n{my_car.get_descriptive_name()}")
my_car.read_odometer()
my_car.fuel_tank.read_fuel_level()
my_car.fuel_tank.fill_tank()
my_car.drive(165)
