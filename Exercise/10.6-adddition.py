while True:
	try:
		a = int(input("First number: "))
		b = int(input("Second Number: "))
		add = a + b
	except ValueError:
		print("can't")
	else:
		print(add)