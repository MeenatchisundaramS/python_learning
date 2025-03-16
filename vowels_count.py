#get number from user those many time get character and find how much vowels print it on console

def count(num):
	vowels="aeiouAEIOU"
	count=0
	
	for i in range(num):
		character=input(f"Enter the letters {i+1} : ")
		if character in vowels:
			count+=1

	print(count)

num=int(input("Enter the number : "))
count(num)

