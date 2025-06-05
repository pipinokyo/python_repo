# What is the expected output of the following code?

x = 1 / 2 + 3 // 3 + 4 ** 2
print(x)

# Step-by-Step Breakdown:
# 1. Operator Precedence (Order of Evaluation)
# Python evaluates the expression left-to-right following operator precedence:

# ** (Exponentiation) → Highest priority
# // (Floor Division), / (Division) → Next priority
# + (Addition) → Lowest priority

# So the evaluation order is:

# 4 ** 2
# 3 // 3
# 1 / 2

# Final addition of all results.

# 2. Step-by-Step Calculation
# Let’s break it down:
# 4 ** 2 (Exponentiation)
# 4 ** 2 → 16

# Now the expression becomes:

# x = 1 / 2 + 3 // 3 + 16
# 3 // 3 (Floor Division)
# 3 // 3 → 1 (since 3 ÷ 3 = 1.0, floor division truncates to 1)

# Now the expression becomes:

# x = 1 / 2 + 1 + 16
# 1 / 2 (Division)
# 1 / 2 → 0.5 (floating-point division)

# Now the expression becomes:
# x = 0.5 + 1 + 16

# Final Addition (0.5 + 1 + 16)
# 0.5 + 1 → 1.5
# 1.5 + 16 → 17.5


# Visualization:
# Original: x = 1 / 2 + 3 // 3 + 4 ** 2

# Step 1: 4 ** 2 → 16
#         x = 1 / 2 + 3 // 3 + 16

# Step 2: 3 // 3 → 1
#         x = 1 / 2 + 1 + 16

# Step 3: 1 / 2 → 0.5
#         x = 0.5 + 1 + 16

# Step 4: 0.5 + 1 → 1.5
#         1.5 + 16 → 17.5

# Final Output: 17.5