#get the number from user and identify if the number is less than Hundred 

def check(num):
	if num<100:
		print(f"The number {num} is less than 100")
	else:
		print(f"The number {num} is equal or greater than 100")

user_num=int(input("Enter the number : "))
check(num=user_num)