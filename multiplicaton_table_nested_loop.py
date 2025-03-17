#Write a program that prints the multiplication table from 1 to 5 using a nested for loop

def nested_loop():
	for i in range(1,5):
		for j in range(1,16):
			print(f"{j} * {i} = {i*j}")
		print()

nested_loop()
