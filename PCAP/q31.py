# What is the expected output of the following code?
x = True  
y = False  
z = False  

if not x or y:  
    print(1)  
elif not x or not y and z:  
    print(2)  
elif not x or y or not y and x:  
    print(3)  
else:  
    print(4)

# Explanation Step by Step:

# Variable Initialization:
# x = True
# y = False
# z = False
# First Condition (if not x or y):
# not x evaluates to False (since x is True).
# y is False.
# The expression becomes False or False, which evaluates to False.
# The condition is not met, so the code moves to the next elif.
# Second Condition (elif not x or not y and z):
# not x is False.
# not y is True (since y is False).
# z is False.
# The expression becomes False or (True and False), which simplifies to False or False and evaluates to False.
# The condition is not met, so the code moves to the next elif.
# Third Condition (elif not x or y or not y and x):
# not x is False.
# y is False.
# not y is True.
# x is True.
# The expression becomes False or False or (True and True), which simplifies to False or False or True and evaluates to True.
# The condition is met, so 3 is printed.

# Output:
# The program prints 3 and exits without evaluating the else clause.

# Final Output:
# 3