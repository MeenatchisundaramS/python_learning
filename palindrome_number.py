#get number from user and find palindrome number for loop

def palindrome(num):
	reverse=0
	temp=num
	count=len(str(num))
	for i in range(count):
		last_digit=temp%10
		reverse=reverse*10+last_digit
		temp=temp//10

	if reverse==num:
		print(f"The number {num} is palindrome number")
	else:
		print(f"The number {num} is not palindrome number")

user_num=int(input("Enter the number : "))
palindrome(num=user_num)
