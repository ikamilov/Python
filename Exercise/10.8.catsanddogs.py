def pets(filename):
	try:
		with open(filename) as file_object:
			file = file_object.read()
	except FileNotFoundError:
		print("File " + filename + " is not existing")
	else:
		print(file)

filenames = ['../cats.txt', 'dogs.txt']
for filename in filenames:
	pets(filename)