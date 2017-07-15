filename = 'guests.txt'

with open(filename, 'a') as file_object:
	for i in range(1,5):
		name = input("Enter Name: ")
		message = "Hello, " + name.title() + " Welcome to XXX Hotel. \n"
		guest = file_object.write(message)
	