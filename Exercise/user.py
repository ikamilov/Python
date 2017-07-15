class User():
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name
		self.name = first_name.title() + " " + last_name.title()
		self.login_attempts = 0

	def describe_user(self):
		print(self.first_name.title() + " " + 
		self.last_name.title() + " using computer a lot.")

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attemts(self):
		self.login_attempts = 0		

	def greet_user(self):
		print("Hello, " + self.name + "!")
		print("Attemted: " + str(self.login_attempts))
class Privileges():
	def __init__(self):
		self.privileges = "can edit"
	def show_privileges(self):
		print("\tPrivileges: " + self.privileges)

class Admin(User):
	def __init__(self, first_name, last_name):
		super().__init__(first_name, last_name)
		self.privilege = Privileges()
