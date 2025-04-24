# What is the expected output of the following code?

data = [261, 321]
try:
    print(data[-3])
except Exception as exception:
    print(exception.args)
else:
    print("('success',)")


# Initialization:
# data = [261, 321]
# Creates a list with two elements:

# Index:   0    1
# Value: 261  321
# Try Block:

# try:
#     print(data[-3])
# Attempts to access data[-3] (the 3rd element from the end)

# Our list only has 2 elements, so valid negative indices are -1 and -2

# This will raise an IndexError because -3 is out of range

# Exception Handling:

# python
# except Exception as exception:
#     print(exception.args)
# Catches the IndexError (which is a subclass of Exception)

# Prints the exception arguments (exception.args)

# For IndexError, this typically contains a tuple with the error message

# Else Block (skipped in this case):


# else:
#     print("('success',)")
# The else block only executes if no exception occurs

# Since we got an exception, this block is skipped

# Expected Output
# The code will output:

# ('list index out of range',)