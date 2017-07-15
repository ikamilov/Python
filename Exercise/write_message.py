filename = 'programming.txt'

with open(filename, 'a') as file_object:
	for i in range(1,3):
		n = input("what do you love")
		file = file_object.write(n + "\n")
