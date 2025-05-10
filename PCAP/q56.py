# What is the expected output of the following code?

z = y = x = 1
print(x, y, z, sep='*')


# Understanding the Code
# Chained Assignment:
# z = y = x = 1 is a chained assignment in Python.

# It assigns the value 1 to x, then assigns x (which is now 1) to y, and finally assigns y (which is 1) to z.

# All three variables (x, y, z) end up with the value 1.

# Print Statement:

# print(x, y, z, sep='*') prints the values of x, y, and z separated by * (instead of the default space).

# Step-by-Step Execution
# Assignment:

# x = 1 → x is now 1.

# y = x → y is now 1 (same as x).

# z = y → z is now 1 (same as y).

# Printing:
# print(x, y, z, sep='*') prints 1, 1, 1 with * as the separator.

# The output is 1*1*1.

# Visualization
# Step 1: x = 1
#    x → 1

# Step 2: y = x (which is 1)
#    y → 1

# Step 3: z = y (which is 1)
#    z → 1

# Final state:
#    x = 1, y = 1, z = 1

# print(x, y, z, sep='*') → "1*1*1"

# Expected Output
# When you run the code:

# z = y = x = 1
# print(x, y, z, sep='*')
# The output will be:
# 1*1*1