#write a program get number from user identify the choolate rate

def rate(num):
	dairy_milk=150
	milky_bar=100
	five_star=50

	if num>0 and num==50:
		print(f"the fivestar rate is {num}, you have purshased to it!")
	elif num==100:
		print(f"Your amount is 100! you have 2 choise of chocolate to purchase. Milkybar(100) and two fivestar(50)")
	elif num==150:
		print(f"Your amount is 150! you have 3 choise of chocolate to purchase. dairymilk(150), Milkybar(100) and  Three fivestar(50)")
	else:
		print("Your amount is too rated!")

user_num=int(input("Enter the amount : "))
rate(num=user_num) 
