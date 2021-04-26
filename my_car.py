from car import Car

my_new_car = Car('audi', 'a4', 2021)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# The import statement tells Python to open the car module and import the class "Car". Now we can use the Car class as if it were defined in this file. 
# Importing classes is an effective way to program

# Storing multiple Classes in a module:
# You can store as many classes as you need in a single module, although each class in a module should be related somehow. 
# The classes Battery and ElectricCar both help represen cars, so let's add them to the module car.py:
# Now we can make a new file called my_electric_car.py, import the ElectricCar class, and make an electric car:

