# get a number from user and identify the last digit of it

def find(num):
	last_digit=num%10
	print(f"The last digit of the number {num} is : {last_digit}")

user_num=int(input("Enter the number : "))
find(num=user_num)