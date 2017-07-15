import json

def get_stored_username():
	"""Get Stored Username"""
	filename = 'numbers.json'
	try:
		with open(filename) as file_object:
			username = json.load(file_object)
	except FileNotFoundError:
		return None
	else:
		return username

def get_new_username():
	username = input("What is your name? ")
	filename = 'numbers.json'
	with open(filename, 'w') as file_object:
		json.dump(username, file_object)
	return username

def greet_user():
	"""Greet the User by Name"""
	username = get_stored_username()
	if username:
		ask = input("Are you " + username + "?")
		if ask == 'yes':
			print("Welcome back, " + username + "!")
		else:
			get_new_username()
	else: 
		username = get_new_username()
		print("We'll remmeber you when you come back, " + username + "!")

greet_user()
