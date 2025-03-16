#get a  number from user and identify the greaterthan ten and lessthan twenty number

def check(num):
	if num>10 and num<20:
		print(f"The given number {num} is greater than 10 and lessthan20")
	else:
		print(f"The given number {num} is not greater than 10 and less than 20")

user_num=int(input("Enter the number : "))
check(num=user_num)