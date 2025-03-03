def triangle_pattern(num):
	for i in range(num,0,-1):
		print(i * "*")

user_num=int(input("Enter the number : "))
triangle_pattern(num=user_num)