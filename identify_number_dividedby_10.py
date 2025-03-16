# geta a number from user and identify the number is divide by ten

def check(num):
	if num%10==0:
		print(f"The number {num} is divided by 10")
	else:
		print(f"The number {num} is not divided by 10")

user_num=int(input("Enter the number : "))
check(num=user_num)
