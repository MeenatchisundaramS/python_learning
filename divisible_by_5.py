#get Number from user those many times get number and add them divisible by five print it on console


def divisible(number):
	num=0
	for i in range(number):
		num+=int(input(f"Enter the number {i+1} : "))

	if num%5==0:
		print(f"The number {num} is divisible by 5")
	else:
		print(f"The number {num} is not divisible by 5")

user_number=int(input("Enter the number : "))
divisible(number=user_number)





