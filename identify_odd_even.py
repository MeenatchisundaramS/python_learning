#get a number from user and identify the odd number or even number

def find(num):
	if num%2==0:
		print(f"The number {num} is even")
	else:
		print(f"The number {num} is odd")

user_num=int(input("Enter the number : "))
find(num=user_num)