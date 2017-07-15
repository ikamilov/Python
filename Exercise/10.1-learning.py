filename = 'learning_python.txt'
with open(filename) as file_object:
	file = file_object.read()
	for i in range(1,4):
		print(file.replace('Python', 'C'))

