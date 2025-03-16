#get Number From user and print L shape star

def pattern(num):
	for i in range(num):
		for j in range(num):
			if i==num-1 or j==0:
				print("*",end=" ")
			else:
				print(" ",end=" ")
		print()

user_num=int(input("Enter the number : "))
pattern(num=user_num)