print("Enter the values for each side of the triangle: ")

one = ""
two = ""
three = ""

while(one != "quit" and two != "quit" and three != "quit"):
	try:
		one = int(input("Enter a side: "))
		two = int(input("Enter another side: "))
		three = int(input("Enter the final side: "))
	except ValueError:
		print("Invalid input")
		continue
	if(one ** 2 + two ** 2 == three ** 2):
		print("It is a triple!")
	elif(one ** 2 + three ** 2 == two ** 2):
		print("It is a triple!")
	elif(two ** 2 + three ** 2 == one ** 2):
		print("It is a triple!")
	else:
		print("Not a triple :(")

	continue
