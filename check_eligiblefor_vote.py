# Write a program that gets a age from user and identify if they can vote or not 

def check(age):
	if age>=18:
		print("You are eligible for vote")
	elif age>0 and age<18:
		print("You are not eligible for vote")
	else:
		print("Please enter valid image")

user_age=int(input("Enter your age"))
check(age=user_age)