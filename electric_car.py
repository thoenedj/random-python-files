# Inheritance
# If the class you're writing is a specialized version of another class you wrote, you can use "inheritance". 
# When one class inherits from another, it takes on the attributes and methods of the first class.
# The original class is called the "parent class" and the new class is called the "child class". 
# The child class can inherit any or all of the attributes and methods of its parent class, but it's also free to define new attributes and methods of its own.

# The __init__() Method for a Child Class
# When you're writing a new class based on an existing class, you'll often want to call the __init__() method from the parent class. 
    # This will initialize any attributes that were defined in the parent __init__() method and make them available in the child class. 

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 23

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to a given value.
        Reject the change if it attempts to roll back the odometer.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the Parent Class."""
        super().__init__(make, model, year)

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())

# When you create a child class, the parent class must be part of the current file and must appear before the child class in the file.
# We define the child class ElectricCar. Here, the name of the parent class must be included in parentheses in the definition of a child class.
# Next, the "def __init__(self, make, model, year)" method takes in the information required to make a Car instance. 
# The super() function is a special function that allows you to call a method from the parent class. 
    # This line tells Python to call the __init__() method from Car, which gives an ElectricCar instance all the attributes defined in that method. 
# Then we make an instance of the ElectricCar class and assign it to my_tesla. 
    # This line calls the __init__() method defined in ElectricCar, which in turn tells Python to call the __init__() method defined in the parent class Car.
# Aside from __init__(), there are no attributes or methods yet that are assigned to an electric car

# Defining Attributes and Methods for the Child Class:
# Once you have a child class that inherits from the parent class, you can add any new attributes and methods necessary to differentiate the child class from the parent class.
# Let's add an attribute that's specific to electric cars (a battery, for example) and a method to report on this attribute:


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the Parent Class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

# Here we add a new attribute "self.battery_size" and set its initial value to, say, 75.
# This value will be associated with all instances created from the ElectricCar class, but won't be associated with any instances of Car. 
# We also added a method called describe_battery() that prints information about the battery.

# Overriding Methods from the Parent Class
# You can override any method from the parent class that doesn't fit what you're trying to model with the child class. 
# To do this, you define a method in the child class with the same name as the method you want to override in the parent class.
# Python will disregard the parent class method and only pay attention to the method you define in the child class.
    # Say the Car class had a method called fill_gas_tank(). This method is meaningless for an all-electric vehicle, so you might want to override this method:

    # class ElectricCar(Car):
        # --snip--

        # def fill_gas_tank(self):
            # """Electric crs don't have gas tanks."""
            # print("This car doesn't need a gas tank!")

# Instances as Attributes:
# You can break an overly large class into smaller classes that work together. 
# For example, if we continue adding detail to the ElectricCar class, we might notice that we're adding many attributes and methods specific to the car's battery.
# When this happens, we can stop and move those attributes and methods to a separate class called "Battery".

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 23

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to a given value.
        Reject the change if it attempts to roll back the odometer.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")


class Battery():
    """A simple attempt to model a battery for an elextric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the Parent Class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()

# Here we define a new class called Battery that doesn't inherit from any other class. The __init__() method has one parameter: battery_size, in addition to self. 
# This is an optional parameter that sets the battery size to 75 if no value is provided. 
# Also, the method describe_battery() has been moved to this class too
# In the ElectricCar class we now add an attribute called self.battery 
    # This tells Python to create a new instance of Battery and assign that instance to the attribute self.battery.
    # This will happen every time the __init__() method is called; any ElectriCar instance will now have a Battery instance created automatically. 
# We then create an electric car and assign it to the variable my_tesla. 
# When we want to describe the battery, we need to work through the car's battery attribute:
    # my_tesla.battery.describe_battery()
# This line tells Python to look at the instance my_tesla, find its battery attribute, and call the method describe_battery() that's associated with the Battery instance stored in the attribute. 
# This seems like a lot of work, but now we can describe the battery in as much detail as we want without cluttering the ElectricCar class. 
# Let's add another method to Battery that reports the range of the car based on the battery size:

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 23

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to a given value.
        Reject the change if it attempts to roll back the odometer.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")


class Battery():
    """A simple attempt to model a battery for an elextric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

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


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the Parent Class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

# my_tesla = ElectricCar('tesla', 'model s', 2019)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()

# Add a method to the Battery class called "upgrade_battery." This method should check the battery size and set the capacity to 100 if it isn't already.
# Make an electric car with a default battery size, call get_range() once, and then call get_range() a second time after upgrading the battery. 
# You should see an increase in the car's battery size. 

new_tesla = ElectricCar('tesla', 'model s', '2021')
new_tesla.get_descriptive_name()
new_tesla.battery.get_range()
new_tesla.battery.upgrade_battery()
new_tesla.battery.get_range()