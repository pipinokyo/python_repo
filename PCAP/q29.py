# What is the expected output of the following code if the user enters 2 and 4?
x = input()
y = input()
print(x + y)

# Expected Output When User Enters 2 and 4
# The correct answer is D. 24

# Explanation
# Input Handling:

# In Python, the input() function always returns a string, even if the user enters numbers.

# When the user enters "2" and "4", these are stored as strings, not numbers.

# String Concatenation:

# The + operator between two strings performs concatenation (joining them together).

# So "2" + "4" results in "24", not the mathematical sum 6.

# Visualization:

# User enters: 2 [Enter] 4 [Enter]

# Memory:
# x = "2" (string)
# y = "4" (string)

# Operation:
# x + y = "2" + "4" = "24"

# Output:
# 24