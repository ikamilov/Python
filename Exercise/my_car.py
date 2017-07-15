import car 
my_tesla = car.Electric_Car('tesla', 'model s', 2016)
print("\n" + my_tesla.get_desriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
my_tesla.fill_gas_tank()

my_car = car.Electric_Car('tesla', 'roadster', 2016)
print(my_car.get_desriptive_name())
my_new_car = car.Car('toyota', 'camry', '2017')
print("\n" + my_new_car.get_desriptive_name())
my_new_car.update_odometer(23)
my_new_car.read_odometer()

my_new_car.increment_odometer(100)
my_new_car.read_odometer()

my_new_car.update_odometer(2)
my_new_car.read_odometer()
