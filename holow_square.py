#get number from user and print holo square star print it on console

def square(num):
	for i in range(num):
		for j in range(num):
			if i==0 or i==num-1:
				print("*",end=" ")
			elif j==0 or j==num-1:
				print("*",end=" ")
			else:
				print(" ",end=" ")

		print()

user_num=int(input("Enter the number : "))
square(num=user_num)