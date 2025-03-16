#get number from user those many time get character and find how much vowels print it on console

def vowels(letter):
	vowels="aeiouAEIOU"
	if letter in vowels:
		print("It is vowels")
	else:
		print("It is not vowels")

user_letter=input("Enter the letter : ")
vowels(letter=user_letter)