First_number_string = input("please enter the first number:")
First_number = int (First_number_string)

Second_number_string = input("Please enter the second number")
Second_number = int(Second_number_string)

operation_list = ["+", "-", "*", "/" ]

Maths_operation = input (f"please enter maths operation:{operation_list}")

if Maths_operation == '+':
    print (First_number + Second_number)
elif Maths_operation == '-':
    print (First_number - Second_number)
elif Maths_operation == '*':
    print (First_number * Second_number)
elif Maths_operation == '/':
    print (First_number / Second_number) 