#get number from user and those many time get number and find largest number for loop

def largest(num):
	largest=1
	for i in range(num):
		number=int(input(f"Enter the number {i+1} : "))
		if number>largest:
			largest=number

	print(largest)

user_num=int(input("Enter the number : "))
largest(num=user_num)

