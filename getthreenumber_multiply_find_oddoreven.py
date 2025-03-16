#get a three number from user and multiple them if it is identify the even number

def multiply(num1,num2,num3):
	num=num1*num2*num3
	print(f"The multiplication of three number is : {num}")
	if num%2==0:
		print(f"The number {num} is even")
	else:
		print(f"The number {num} is odd")

user_num1=int(input("Enter the number 1 : "))
user_num2=int(input("Enter the number 2 : "))
user_num3=int(input("Enter the number 3 : "))
multiply(num1=user_num1,num2=user_num2,num3=user_num3)
