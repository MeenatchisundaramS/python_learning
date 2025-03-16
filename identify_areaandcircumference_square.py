# get a one side of square from user and identify the area and circumference of square

def square(side):
	area=side*side
	print(f"The area of the square is : {area}")
	circumference=4*side
	print(f"The circumference of the square is : {circumference}")

user_side=int(input("Enter the one side of square : "))
square(side=user_side)
