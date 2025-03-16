#write a program get two number from user and remainder them identify odd number

def remainder(num1,num2):
	remainder=double(num1/num2)
	if remainder%2!=0:
		print(f"The remainder {remainder} is Odd number")
	else:
		print(f"The remainder {remainder} is Even number")

user_num1=int(input("Enter the number 1 : "))
user_num2=int(input("Enter the number 2 : "))
remainder(num1=user_num1,num2=user_num2)