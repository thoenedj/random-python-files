class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

my_new_car = Car('hyundai', 'elantra', '2012')
print(my_new_car.get_descriptive_name())

# As in the "Dog" class, we define the __init__() method with the self parameter first.
# We also give it three other parameters: make, model, and year.
# The __init__() method takes in these parameters and assigns them to the attributes that will be associated with instances made from this class. 
# When we make a new Car instance, we'll need to specify a make, model, and year for our instance.

# Then we define another method called "get_descriptive_name()" that puts a car's year, make, and model into one string neatly describing the car.
# To work with the attributes in this method, we use self.make, self.model, and self.year.

# Then we make an instance from the Car class and assign it to the variable my_new_car. 
# Then we call get_descriptive_name() to show what kind of car we have. 


# Setting a default value for an attribute:
# When an instance is created, attributes can be defined without being passed in as parameters. 
# These attributes can be defined in the __init__() method, where they are assigned a default value.

# Let's add an attribute called odometer_reading that always starts with a value of 0. We'll also add a method read_odometer() that helps us read each car's odometer. 

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

my_new_car = Car('hyundai', 'elantra', '2012')
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()


# Modifying attribute values:
# You can change an attribute's value in three ways: you can change it directly through an instance; set the value through a method; or increment the value through a method.
# Let's look at each of these approaches.

# Modifying an attribute's value directly:
# The simplest way to modify the value of an attribute is to access the attribute directly through an instance:

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# Modifying an Attribute's Value through a Method:
# You can pass the new value to a method that handles the updating internally:

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to a given value."""
        self.odometer_reading = mileage

my_new_car = Car('hyundai', 'elantra', '2012')
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(27)
my_new_car.read_odometer()

# Let's add a little logic to make sure no one tries to roll back the odometer reading:

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

my_new_car = Car('hyundai', 'elantra', '2012')
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(21)


# Incrementing an Attribute's Value through a Method:
# Say we buy a used car and put 100 miles on it between the time we buy it and the time we register it.
# Here's a method that allows us to pass this incremental amount and add that value to the odometer reading:

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

my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(-100)
my_used_car.read_odometer()


# Inheritance
# If the class you're writing is a specialized version of another class you wrote, you can use "inheritance". 
# When one class inherits from another, it takes on the attributes and methods of the first class.
# The original class is called the "parent class" and the new class is called the "child class". 
# The child class can inherit any or all of the attributes and methods of its parent class, but it's also free to define new attributes and methods of its own.

# The __init__() Method for a Child Class
# When you're writing a new class based on an existing class, you'll often want to call the __init__() method from the parent class. 
    # This will initialize any attributes that were defined in the parent __init__() method and make them available in the child class. 
    