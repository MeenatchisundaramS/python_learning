def num_triangle(num):
	for i in range(1,num+1):
		for j in range(i):
			print(j+1,end=" ")
		print()

user_num=int(input("Enter the number : "))
num_triangle(num=user_num)