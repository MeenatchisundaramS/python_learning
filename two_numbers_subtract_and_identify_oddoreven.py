#get a two number from user and subtract them if it is identify the even number

def subtract(num1,num2):
	num=num1-num2
	print(f"The subtracted value is : {num}")

def evenodd(num1,num2):
	if (num1-num2)%2==0:
		print(f"The number {(num1-num2)} is Even ")
	else:
		print(f"The number {(num1-num2)} is Odd ")

user_num1=int(input("Enter the number1 : "))
user_num2=int(input("Enter the number 2 : "))
subtract(num1=user_num1,num2=user_num2)
evenodd(num1=user_num1,num2=user_num2)