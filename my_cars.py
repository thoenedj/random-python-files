from car import Car, ElectricCar

my_beetle = Car('volkswagon', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

# Here we imported multiple classes from a module

# Importing an entire module:
# You can also import an entire module and then access the classes you need using dot notation. 
# This approach is simple and results in code that is easy to read. 
# Because every call that creates an instance of a class includes the module name, you won't have naming conflicts with any names used in the current file.

import car 

my_beetle = Car('volkswagon', 'beetle', 2021)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2021)
print(my_tesla.get_descriptive_name())

# Using Aliases
# Aliases can be quite helpful when using modules to organize your project's code. 
# As an example, consider a program where you want to make a bunch of electric cars. It might get tedious to type (and read) ElectricCar over and over again.
# You can give ElectricCar an alias in the import statement:

from car import ElectricCar as EC 

# Now you can use this alias whenever you want to make an electrc car:

my_new_tesla = EC('tesla', 'model s', 2020)
print(my_new_tesla.get_descriptive_name())