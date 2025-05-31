# What is the expected behavior of the following snippet?

x = 1
def a(x):
    return 2 * x


x = 2 + a(x)
print(a(x))


# Step-by-Step Execution:
# Initial Assignment:

# x = 1 sets the global variable x to 1

# Function Definition:

# def a(x): return 2 * x creates a function that:

# Takes a parameter x (this is a different x than the global variable)

# Returns 2 * x (whatever x is passed to it)

# First Function Call (a(x) in x = 2 + a(x)):

# The global x is 1, so a(1) is called

# Inside function a, parameter x becomes 1

# return 2 * 1 → returns 2

# Now x = 2 + 2 → global x becomes 4

# Second Function Call (print(a(x))):

# Now global x is 4, so a(4) is called

# Inside function a, parameter x becomes 4

# return 2 * 4 → returns 8

# print(8) outputs 8