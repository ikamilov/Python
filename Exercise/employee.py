class Employee():
	def __init__(self, first, last, salary):
		self.first = first
		self.last = last
		self.salary = salary

	def give_raise(self):
		self.salary = self.salary + 5000

	def give_custom_raise(self, custom):
		self.salary = self.salary + custom

	def show_info(self):
		print("Name: " + self.first.title() + " " + self.last.title())
		print("Total salary: " + str(self.salary))