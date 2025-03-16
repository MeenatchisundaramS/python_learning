#Write a program to get girls name a to z and print name

def findname(letter):
	if letter=="a" or letter=="A":
		print("Anjali")
	elif letter=="b" or letter=="B":
		print("Baby")
	elif letter=="c" or letter=="C":
		print("Chithra")
	elif letter=="d" or letter=="D":
		print("Dhanu")
	elif letter=="e" or letter=="E":
		print("Elakiya")
	elif letter=="f" or letter=="F":
		print("Fathima")
	elif letter=="g" or letter=="G":
		print("Gayu")
	elif letter=="h" or letter=="H":
		print("Hasini")
	elif letter=="i" or letter=="I":
		print("Indhu")
	elif letter=="j" or letter=="J":
		print("Jasmine")
	elif letter=="k" or letter=="K":
		print("Kalai")
	elif letter=="l" or letter=="L":
		print("Leka")
	elif letter=="m" or letter=="M":
		print("Madhu")
	elif letter=="n" or letter=="N":
		print("Narmadha")
	elif letter=="o" or letter=="O":
		print("Oviya")
	elif letter=="p" or letter=="P":
		print("Pavi")
	elif letter=="q" or letter=="Q":
		print("Queen")
	elif letter=="r" or letter=="R":
		print("Rashmika")
	elif letter=="s" or letter=="S":
		print("Sumithra")
	elif letter=="t" or letter=="T":
		print("Tharshika")
	elif letter=="u" or letter=="U":
		print("Uyir")
	elif letter=="v" or letter=="V":
		print("Vaishu")
	elif letter=="w" or letter=="W":
		print("Wowri")
	elif letter=="x" or letter=="X":
		print("Xevior")
	elif letter=="y" or letter=="Y":
		print("Yasika")
	elif letter=="z" or letter=="Z":
		print("Ziksa")
	else:
		print("Please enter valid letter A-Z !")

user_letter=input("Enter the letter : ")
findname(letter=user_letter)