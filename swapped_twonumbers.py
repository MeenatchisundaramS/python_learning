#get two input from the user and swapped two numbers

def swap(num1,num2):
	temp=num1
	num1=num2
	num2=temp
	print(f"After swapping the number 1 is {num1}, the number 2 is {num2}")

user_num1=int(input("Enter the number 1 : "))
user_num2=int(input("Enter the number 2 : "))
swap(num1=user_num1,num2=user_num2)