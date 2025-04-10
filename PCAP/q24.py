# What will be the output of the following code snippet?
x = 2          # Line 1
y = 1          # Line 2
x *= y + 1     # Line 3
print(x)       # Line 4


# Step-by-Step Execution
# Line 1: Variable Assignment
# x = 2
# Visualization:
# x = 2
# Line 2: Variable Assignment
# y = 1
# Visualization:
# x = 2
# y = 1

# Line 3: Compound Assignment Operation
# x *= y + 1
# This line is equivalent to x = x * (y + 1) because the + operator has higher precedence than *=.
# Let's break it down:
# First, evaluate y + 1: 1 + 1 = 2
# Then multiply x by this result: 2 * 2 = 4
# Finally, assign this back to x

# Visualization:
# Before operation:
# x = 2
# y = 1

# Operation steps:
# 1. y + 1 → 1 + 1 → 2
# 2. x * (result) → 2 * 2 → 4
# 3. x = 4

# After operation:
# x = 4
# y = 1

# Line 4: Print Operation
# print(x)
# This prints the current value of x, which is 4.