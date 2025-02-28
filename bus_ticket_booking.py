"""Bus Ticket Booking System
 Ask the user for:

Passenger Name
Bus Number
Seat Type (Normal ₹200, Sleeper ₹500, AC ₹800)
 Display the final ticket price."""

def bus_ticket_booking(name,bus_number,seat_type):
	ticket_price=0
	if seat_type=="Normal":
		ticket_price=200
	elif seat_type=="Sleeper":
		ticket_price=500
	elif seat_type=="AC":
		ticket_price=800
	else:
		return "Please Enter valid Seat Type"

	return ticket_price


user_name=input("Enter your name : ")
user_bus_number=int(input("Enter your bus number : "))
user_seat_type=input("Enter your seat type (Normal/Sleeper/AC) : ")

ticket_price=bus_ticket_booking(name=user_name,bus_number=user_bus_number,seat_type=user_seat_type)

def display():
	print(f"Your name is {user_name}")
	print(f"Your bus number is {user_bus_number}")
	print(f"Your Seat type is {user_seat_type}")
	print(f"Your ticket price is {ticket_price}")

print(bus_ticket_booking(name=user_name,bus_number=user_bus_number,seat_type=user_seat_type))
display()