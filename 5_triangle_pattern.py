def triangle_pattern(num):
	for i in range(num,0,-1):
		print(" " * (num-i) + "*" * (2*i-1))

user_num=int(input("Enter the number : "))
triangle_pattern(num=user_num)