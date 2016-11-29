#
# Shane Bishop
# 101030053
#
# Reference List:
# Gaddis, T. (2015). "Starting Out With Python"
#

# Provide list of supported operations
print("(A)ddition")
print("(S)ubtraction")
print("(M)ultiplication")
print("(D)ivision (Long)")

# Ask the user for operation to perofmr
operation_chosen = input("\nPlease select an operation from the list above: ").upper()

# Perform operation as specified by the user and print the result
if operation_chosen == "A" or operation_chosen == "ADDITION":
	first_int  = int(input("Please provide the 1st integer: "))
	second_int = int(input("Plesae provide the 2nd integer: "))
	
	print(first_int, "+", second_int, "=", first_int + second_int)
elif operation_chosen == "S" or operation_chosen == "SUBTRACTION":
	first_int  = int(input("Please provide the 1st integer: "))
	second_int = int(input("Plesae provide the 2nd integer: "))
	
	print(first_int, "-", second_int, "=", first_int - second_int)
elif operation_chosen == "M" or operation_chosen == "MULTIPLICATION":
	first_int  = int(input("Please provide the 1st integer: "))
	second_int = int(input("Plesae provide the 2nd integer: "))
	
	print(first_int, "*", second_int, "=", first_int * second_int)
elif operation_chosen == "D" or operation_chosen == "DIVISION":
	first_int  = int(input("Please provide the 1st integer: "))
	second_int = int(input("Plesae provide the 2nd integer: "))
	
	print(first_int, "/", second_int, "=", first_int / second_int)
# If none of the above blocks are executed, the user entered an unsupported operation
else:
	print("This program does not support the operation '", operation_chosen, "'.", sep="")