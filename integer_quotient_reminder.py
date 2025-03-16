#get two integer number, quotient and reminder them and print it on console

def quotient(num1,num2):
	quotient=num1/num2
	print(f"The quotient of the two value is : {quotient}")

def remainder(num1,num2):
	remainder=num1%num2
	print(f"The remainder of the two value is : {remainder}")

user_num1=int(input("Enter the number 1 : "))
user_num2=int(input("Enter the number 2 : "))
quotient(num1=user_num1,num2=user_num2)
remainder(num1=user_num1,num2=user_num2)