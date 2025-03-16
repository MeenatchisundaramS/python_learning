#get a two number from user and divide and find reminder  them if it is identify the even number

def remainder(num1,num2):
	num=num1%num2
	print(f"The reminder of the two value is : {num}")
	if num%2==0:
		print(f"The number {num} is even")
	else:
		print(f"The number {num} is odd")

user_num1=int(input("Enter the number 1 : "))
user_num2=int(input("Enter the number 2 : "))
remainder(num1=user_num1,num2=user_num2)