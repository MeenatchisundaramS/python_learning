#get a number from user and identify the Amstrong number


def armstrong(num):
	temp=str(num)
	digit=len(temp)
	sum=0
	for i in range(num):
		square=int(i)**digit
		sum+=square
	if sum==num:
		print(f"The number {num} is armstrong number")
	else:
		print(f"The number {num} is not armstrong number")

user_num=int(input("Enter the number : "))
armstrong(num=user_num)