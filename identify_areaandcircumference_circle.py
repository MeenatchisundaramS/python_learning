#get a radius from user and identify the area and circumference of circle

def circle(radius):
	pie=3.14
	area=pie*radius**2
	print(f"The area of circle is : {area}")
	circumference=2*pie*radius
	print(f"The circumference of the circle is : {circumference}")

user_radius=int(input("Enter the radius of the circle : "))
circle(radius=user_radius)