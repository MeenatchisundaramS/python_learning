"""Problem Statement:
You are developing a Bank Loan Eligibility System for a bank. The system should take user details and analyze whether they qualify for a loan based on predefined conditions.

Requirements:
The system should prompt the user to enter:

Name (String)
Age (Integer)
Monthly Income (Integer)
Loan Amount Requested (Integer)
Credit Score (Integer between 300-850)
Number of Previous Loans Taken (Integer)
Eligibility Criteria:

A person must be at least 21 years old to apply for a loan.
The monthly income must be greater than the requested loan amount divided by 10 (e.g., if a user requests ₹50,000, their income should be at least ₹5,000).
If the credit score is above 750, the user is eligible.
If the credit score is between 600 and 750, eligibility depends on the number of previous loans:
If the person has taken 2 or more loans, they are not eligible.
If they have less than 2 loans, they are eligible.
If the credit score is below 600, the user is not eligible for the loan.
Program Requirements:

Implement the logic using functions.
Use for loops if needed for validation or input handling.
Use if-else and elif conditions for decision-making.
Do not use lists, tuples, sets, dictionaries, or percentage calculations."""

def requirements():
	print("---Please fill the Form---")
	name=input("Enter your name : ")
	age = int(input("Enter your age : "))
	income=int(input("Enter your Monthly income : "))
	loan_amt=int(input("How much loan do you want? : "))
	credit_score=int(input("Enter your credit score(300-850) : "))
	no_previoous_loan=int(input("How many previous loan are you taken? : "))
	return name,age,income,loan_amt,credit_score,no_previoous_loan

name,age,income,loan_amt,credit_score,no_previoous_loan=requirements()

def check_eligibilty(age,income,loan_amt,credit_score,no_previoous_loan):
	if age<21:
		return "Sorry your age is too low!!"
	if income<=(loan_amt//10):
		return "Sorry Your monthly income is lessthan of your loan amount!!"
	if credit_score>750:
		return "You are eligible for the loan"
	elif credit_score>600 and credit_score<=750:
		if no_previous_loan<2:
			return "You are eligible for the loan!!"
		else:
			return "You are not eligible for the loan"
	else:
		return "Sorry your credit score is too low"


print(check_eligibilty(age,income,loan_amt,credit_score,no_previoous_loan))

