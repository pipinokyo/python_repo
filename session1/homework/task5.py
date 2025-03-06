# Task 5: Reverse a Number
# Ask the user to enter a number and print its reverse.
# (Example: If the user enters 1234, the program should print 4321.)

# first receice a number from the user and save it into a variable
# reverse the number and print it 

num = input("enter a number: ")
print(num[::-1])

# num = input("Enter a number: ")
# reversed_num = ""
# for character in num:
#     reversed_num = character + reversed_num
# print("reversed number:", reversed_num)




# if the number was provided as an int we need to convert int to a string
# we can not use slicing or iterate over int. int are not sequences

# Get the integer from the user.
# Convert the integer to a string. num_str = str(num)
# Reverse the string.
# Convert the reversed string back to an integer (optional, depending on the desired output).
# Print the reversed number.