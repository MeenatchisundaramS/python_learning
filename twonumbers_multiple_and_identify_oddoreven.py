#get a two number from user and multilple them if it is identify the even number

def multiply(num1,num2):
	num=num1*num2
	print(f"The multiply of two number is : {num}")
	if num%2==0:
		print(f"The number {num} is even")
	else:
		print(f"The number {num} is odd")

user_num1=int(input("Enter the number 1 : "))
user_num2=int(input("Enter the number 2 : "))
multiply(num1=user_num1,num2=user_num2)