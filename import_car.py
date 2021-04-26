from car import Car, ElectricCar, FuelTank, Battery

my_beetle = Car('volkswagon', 'beetle', 2021)
my_beetle.fuel_tank.tank_size(18)
my_beetle.fuel_tank.add_fuel(10)

# Make lists to hold a fleet of cars.
gas_fleet = []
electric_fleet = []

# Make 250 gas cars and 500 electric cars.
for _ in range(2):
    car = Car('ford', 'escape', 2021)
    gas_fleet.append(car)
for _ in range(5):
    ecar = ElectricCar('nissan', 'leaf', 2021)
    electric_fleet.append(ecar)

# Fill the gas cars, and charge electric cars.
for car in gas_fleet:
    car.fuel_tank.tank_size(15)
    car.fuel_tank.fill_tank()
for ecar in electric_fleet:
    ecar.battery.charge()

print(f"Gas cars: {len(gas_fleet)}")
print(f"Electric Cars: {len(electric_fleet)}")