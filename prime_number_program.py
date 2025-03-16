"""prime number program
prime_number:
			it means the number exactly divisible by one and itself called prime numbers.
			"0" and "1" the both numbers are not prime """

def prime(num):
	if num==0 or num==1:
		print("It is not a prime number")
		return None
	n = 0
	for i in range(2,(num//2)+1):
		# print(f"count {i - 1}")
		n = n + 1
		print(f"The  i count is : {i}")


		if num%i==0:
			print("Its not a prime")
			break

	else:
		print("Its a prime")

	print(f"The loop iteration count is : {n}")
user_num=int(input("Enter the number : "))
prime(num=user_num) 
