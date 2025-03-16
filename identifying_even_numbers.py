#write a program get two number from user and subtraction them identify even numbers

def even_numbers(num1,num2):
	num=num1-num2
	if num%2==0:
		print(f"The number {num} is even number")
	else:
		print(f"The number {num} is not the even number")

user_num1=int(input("Enter the number 1 : "))
user_num2=int(input("Enter the number 2 : "))
even_numbers(num1=user_num1,num2=user_num2)