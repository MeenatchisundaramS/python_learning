#get the number from user and identify if the number is greater than five 

def check(num):
	if num>5:
		print(f"The number {num} is greater than 5")
	elif num<5:
		print(f"The number {num} is less than 5")
	else:
		print(f"The number {num} is equal to 5")

user_num=int(input("Enter the number : "))
check(num=user_num)