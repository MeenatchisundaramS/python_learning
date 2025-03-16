# Get a length and width and identify the area and circumference of rectangular

def rectangular(length,width):
	area=length*width
	print(f"The area of the rectangular is : {area}")
	circumference=2*(length+width)
	print(f"The circumference of the rectangular is : {circumference}")

user_length=int(input("Enter the length of the rectangular : "))
user_width=int(input("Enter the width of the rectangular : "))
rectangular(length=user_length,width=user_width)

