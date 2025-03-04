def rectangle_pattern(num1,num2):
	for i in range(num1):
		for j in range(num2):
			if i==0 or i==num1-1:
				print("*",end=" ")
			elif i>0 or j==0 or j==num2-1:
				print("*",end=" ")
			else:
				print(" ",end=" ")

		print()

user_num1=int(input("Enter the number1 : "))
user_num2=int(input("Enter the number2 : "))
rectangle_pattern(num1=user_num1,num2=user_num2)