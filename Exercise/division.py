print("Give me two numbers, and I'll divide them.")
print("Press 'q' to exit the program.")

while True:
	first_number = input("First number: ")
	if first_number == 'q':
		break
	second_number = input("Second number: ")
	try:
		answer = int(first_number) / int(second_number)
	except ZeroDivisionError:
		print("You can not divide")
	else:
		print(answer)