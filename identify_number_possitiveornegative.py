#get a number from user and identify the positive number or negative number

def check(num):
	if num>=0:
		print(f"The number {num} is possitive")
	else:
		print(f"The number {num} is negative")

user_num=int(input("Enter the number : "))
check(num=user_num)