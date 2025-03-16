#get a number from user and identify the number is greater than hundered or less than fifty

def check(num):
	if num>100 or num<50:
		print(f"The given number {num} condition is true")
	else:
		print(f"The given number {num} condition is false")

user_num=int(input("Enter the number : "))
check(num=user_num) 