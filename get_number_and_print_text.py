#Write a program to get a number from user and print to text

def numtotext(num):
	if num==1:
		print("One")
	elif num==2:
		print("Two")
	elif num==3:
		print("Three")
	elif num==4:
		print("Four")
	elif num==5:
		print("Five")
	elif num==6:
		print("Six")
	elif num==7:
		print("Seven")
	elif num==8:
		print("Eight")
	elif num==9:
		print("Nine")
	elif num==10:
		print("Ten")
	else:
		print("Please valid number upto 1-10")

user_num=int(input("Enter the number between 1-10 : "))
numtotext(num=user_num)