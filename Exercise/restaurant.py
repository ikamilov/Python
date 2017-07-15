class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0
	
	def desribe_restaurant(self):
		print(self.restaurant_name.title() + "'s cuisine type is " + 
			self.cuisine_type.title() + ".")

	def open_restaurant(self):
		print(self.restaurant_name.title() + " is now open.")

	def set_number_served(self, year):
		self.number_served = year

	def years_served(self):
		print(self.restaurant_name.title() + " has served " + str(self.number_served) +
		" years." )

	def increment_number_served(self, number):
		self.number_served += number
class Flavors():
	def __init__(self, flavors = 'Strawberry'):
		self.flavors = flavors

	def desribe_flavor(self):
		print("Ice Cream has a " + self.flavors + " flavor." )

class IceCreamStand(Restaurant):
	def __init__(self, restaurant_name, cuisine_type):
		super().__init__(restaurant_name, cuisine_type)
		self.flavor = Flavors()

	