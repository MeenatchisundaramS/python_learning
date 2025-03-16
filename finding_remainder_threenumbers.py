#write a program and get three number from user and identify the remainder and find odd or even number

def remainder(num1,num2,num3):
	num=num1/num2
	remainder=num/num3
	print(f"The three number {num1},{num2},{num3} remainder is : {remainder}")
	if remainder%2==0:
		print(f"The remainder {remainder} is Even number")
	else:
		print(f"The remainder {remainder} is Odd number")

user_num1=int(input("Enter the number 1 : "))
user_num2=int(input("Enter the number 2 : "))
user_num3=int(input("Enter the number 3 : "))
remainder(num1=user_num1,num2=user_num2,num3=user_num3)