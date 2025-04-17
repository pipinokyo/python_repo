# What is the expected output of the following code?

x = 1
y = 2
x, y, z= x, x, y
z, y, z = x, y, z
print(x, y, z)


# Step-by-Step Execution with Visualization:
# Initial State:
# x = 1
# y = 2
# # Memory: x=1, y=2
# After First Assignment (x, y, z = x, x, y):
# The right side is evaluated first: (x, x, y) → (1, 1, 2)

# Then unpacking occurs:
# x gets 1 (no change)
# y gets 1 (changed from 2 to 1)
# z gets 2 (new variable)

# # Memory after this line:
# x = 1
# y = 1  # changed from 2 to 1
# z = 2  # newly created
# After Second Assignment (z, y, z = x, y, z):
# The right side is evaluated first: (x, y, z) → (1, 1, 2)

# Then unpacking occurs left-to-right:

# z gets 1 (first value) → z is now 1

# y gets 1 (second value) → y remains 1

# z gets 2 (third value) → z changes from 1 to 2


# # Memory after this line:
# x = 1  # unchanged
# y = 1  # unchanged
# z = 2  # final value after reassignment
# Final print(x, y, z):
# Prints the values: 1 1 2

# Visualization Table:
# Line	x	y	z	Comments
# Initial	1	2	-	z doesn't exist yet
# After 1st assign	1	1	2	y changes, z created
# After 2nd assign	1	1	2	z changes twice (1 → 2)
# Key Notes:
# Tuple unpacking is evaluated left-to-right.
# In z, y, z = x, y, z, the first z is assigned before the second z is evaluated.

# First z gets x (1)

# Then y gets y (1)

# Finally, z gets z (2, original value from previous step)

# The right side is fully evaluated before unpacking begins.
# This is why z's original value (2) is used in the final assignment.

# Final Output:

# 1 1 2