#get a age from user and check if he is eligible for marriage

def check(age):
	if age>=18 and age<40:
		print("Eligible for marriage")
	elif age>40:
		print("Too high age")
	else:
		print("Not eligible")

user_age=int(input("Enter the age : "))
check(age=user_age)