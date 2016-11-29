#
# Shane Bishop
# 101030053
#
# Reference List:
# Gaddis, T. (2015). "Starting Out With Python"
#

# Retrieve input from the user
input("Name:           ")
input("Student Number: ")
grade_received = int(input("What was the percentage grade you received? "))

# Initialize output string
print("A grade of ", grade_received, " is in the '", sep="", end="")

# Determine and print the grade
if grade_received < 50:
	print("F' range.")
elif grade_received < 53:
	print("D-' range.")
elif grade_received < 57:
	print("D' range.")
elif grade_received < 60:
	print("D+' range.")
elif grade_received < 63:
	print("C-' range.")
elif grade_received < 67:
	print("C' range.")
elif grade_received < 70:
	print("C+' range.")
elif grade_received < 73:
	print("B-' range.")
elif grade_received < 77:
	print("B' range.")
elif grade_received < 80:
	print("B+' range.")
elif grade_received < 85:
	print("A-' range.")
elif grade_received < 90:
	print("A' range.")
else:
	print("A+' range.")