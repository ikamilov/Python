
def count_words(filename):
	try:
		with open(filename) as file_object:
			file = file_object.read()
	except FileNotFoundError:
		msg = "Sorry the file '" + filename + "' does not exist"
		print(msg)
	else:
		words = file.split()
		num_words = len(words)
		print("This file '" + filename + "' has about " + str(num_words) + " words.")

filenames = ['alice.txt', 'guests.txt', 'example.txt']
for filename in filenames:
	count_words(filename)