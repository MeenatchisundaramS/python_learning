# get a number from user and identify the factors and print it on console

def factors(num):
	factor=1
	for i in range(2,num//2+1):
		if num%i==0:
			print(f"The factor is {i}")
	else:
		print(f"The factor is {factor}")

num=int(input("Enter the number : "))
factors(num)

