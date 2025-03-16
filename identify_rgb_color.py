#write a program get three indiger from user and identify the colour of RGB

def find_rgb(num1,num2,num3):
	white=255,255,255
	red=255,0,0
	blue=0,0,255

	if num1==255 and num2==255 and num3==255:
		print("White color")
	elif  num1==255 and num2==0 and num3==0:
		print("Red color")
	elif num1==0 and num2==0 and num3==255:
		print("Blue color")
	else:
		print("Please valid color number!")

user_num1=int(input("Enter the value of R : "))
user_num2=int(input("Enter the value of G : "))
user_num3=int(input("Enter the value of B : "))
find_rgb(num1=user_num1,num2=user_num2,num3=user_num3)