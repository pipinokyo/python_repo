# What is the expected output of the following code?

def func(x):
    return 1 if x % 2 != 0 else 2

print(func(func(1)))

# This function takes an input x and checks if it is odd (x % 2 != 0).
# If x is odd, it returns 1.
# If x is even, it returns 2.
# The Function Call: func(func(1))
# This is a nested call, so we evaluate it from the inside out.

# Step 1: Evaluate the Inner func(1)
# x = 1 (input to the inner func).
# Check 1 % 2 != 0 → 1 % 2 = 1, so 1 != 0 is True.
# Therefore, the function returns 1.

# Step 2: Now Evaluate func(func(1)) → func(1)
# The result of func(1) was 1, so now we call func(1) again.
# x = 1 (again).
# 1 % 2 != 0 is True, so it returns 1.

# Final Output:
# The outer print(func(func(1))) prints 1.