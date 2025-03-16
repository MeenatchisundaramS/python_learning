#get number from user and find factorial number use for loop method

def factorial(num):
	total=1
	for i in range(2,num+1):
		total=total*i

	return f"The factorial of {num} is : {total}"

user_num=int(input("Enter the number : "))
print(factorial(num=user_num))
