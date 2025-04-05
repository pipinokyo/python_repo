# What is the expected behavior of the following snippet?
x = 1 # line 1
def a(x): # line 2
    return 2 * x # line 3
x = 2 + a(x) # line 4
print(a(x)) # line 5


# Step-by-Step Execution:
# Line 1: x = 1
# Assigns x = 1 (global scope).

# State: x (global) = 1

# Line 2-3: def a(x): return 2 * x
# Defines a function a(x) that takes a parameter x and returns 2 * x.

# The x inside a(x) is local to the function (different from the global x).

# Line 4: x = 2 + a(x)
# Call a(x):

# The current global x is 1, so a(1) is called.

# Inside a(x), x = 1 (local to the function).

# Computes 2 * 1 = 2 and returns it.

# Compute 2 + a(x):

# 2 + 2 = 4

# Update global x:

# Now, x (global) is reassigned to 4.

# State: x (global) = 4

# Line 5: print(a(x))
# Call a(x) again:

# Now, the global x is 4, so a(4) is called.

# Inside a(x), x = 4 (local to the function).

# Computes 2 * 4 = 8 and returns it.

# Print the result:

# print(8) outputs 8.