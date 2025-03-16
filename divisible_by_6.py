#get a number from user those many time get number and add them divisible by six and twelve

def divisible(num):
	total=0
	for i in range(num):
		total+=int(input(f"Enter the number {i+1} : "))

	if total%6==0 and total%12==0:
		print(f"The {total} is divided by 6 and 12")
	else:
		print(f"The {total} is not divided by 6 and 12")


user_num=int(input("Enter the number : "))
divisible(num=user_num)
