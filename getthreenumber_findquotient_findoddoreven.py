#get a three number from user and divide and find quotient  them if it is identify the even number

def quotient(num1,num2,num3):
	quotient=(num1%num2)%num3
	print(f"The quotient of three number is : {quotient}")
	if quotient%2==0:
		print(f"The quotient {quotient} is even ")
	else:
		print(f"The quotient {quotient} is odd ")

user_num1=int(input("Enter the number1 : "))
user_num2=int(input("Enter the number 2 : "))
user_num3=int(input("Enter the number 3 : "))
quotient(num1=user_num1,num2=user_num2,num3=user_num3)