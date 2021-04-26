from car import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2021)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# Importing multiple classes from a module:
# You can import as many classes as you need into a program file. 
# If we want to make a regular car and an electric car in the same file, we need to import both classes, Car and ElectricCar: