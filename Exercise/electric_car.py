from car import Electric_Car

my_car = Electric_Car('tesla', 'model s', 2016)
print(my_car.get_desriptive_name())
my_car.battery.describe_battery()
my_car.battery.get_range()
my_car.battery.upgrade_battery()
my_car.battery.describe_battery()
my_car.battery.get_range()
my_car.fill_gas_tank()
