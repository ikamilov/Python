import json

def stored_number():
	filename = 'numbers.json'	
	try:
		with open(filename) as file_object:
			number = json.load(file_object)
	except FileNotFoundError:
		return None
	else:
		return number

def survey_number():
	number = input("What is your favorite number? ")
	filename = 'numbers.json'
	with open(filename, 'w') as file_object:
		json.dump(number, file_object)
	return number

def favorite_number():
	number = stored_number()
	if number:
		print("I know your favorite number! It's " + number)
	else:
		number = survey_number()
		print("Enter")
favorite_number()