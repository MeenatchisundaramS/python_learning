#get radius and height from user and identify the cone volume and print it on console

def volume(height,radius):
	pie=3.14
	cone_volume=1/3*pie*(radius**2)*height
	print(f"The height {height} and radius {radius} of the cone volume is : {cone_volume}")

user_height=int(input("Enter the height of the cone : "))
user_radius=int(input("Enter the radius of the cone : "))
volume(height=user_height,radius=user_radius)