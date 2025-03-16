#get radius and height from user and identify the cylinder volume and print it on console

def cylinder_volume(height,radius):
	pie=3.14
	volume=int(pie*radius**2*height)
	print(f"The volume of the cylinder is : {volume}")

user_height=int(input("Enter the height of the cylinder : "))
user_radius=int(input("Enter the radius of the cylinder : "))
cylinder_volume(height=user_height,radius=user_radius)