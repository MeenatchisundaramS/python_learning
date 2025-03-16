#get number of windows in class and check if ok to sit there and listen to the mokkai that all members put

def windows_check(number):
	if number>0 and number<=3:
		print("Normal to sit")
	elif number>3 and number<=5:
		print("Okay to sit")
	else:
		print("Not okay to sit")

user_number=int(input("Enter the windows do you want in Classroom : "))
windows_check(number=user_number)
