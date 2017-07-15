# Greet Users
def greet_users(names):
	"""It will show names individually"""
	for name in names:
		print("Hello, " + name.title() + "!")

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
