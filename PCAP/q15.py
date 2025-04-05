# What is the expected behavior of the following snippet?
def fun(a, b=0, c=5, d=1):
    return a ** b ** c
print(fun(b=2, a=2, c=3))


# Function Definition:

# def fun(a, b=0, c=5, d=1):
#     return a ** b ** c
# The function fun takes 4 parameters:

# a: mandatory positional parameter
# b: optional with default value 0
# c: optional with default value 5
# d: optional with default value 1

# The expression a ** b ** c uses exponentiation with right associativity (meaning it's evaluated as a ** (b ** c))

# Function Call:

# print(fun(b=2, a=2, c=3))
# We're passing arguments using keyword arguments (named parameters):

# a = 2
# b = 2
# c = 3
# d is not provided, so it uses the default value 1 (though it's not used in the calculation)

# Evaluation Steps:
# First evaluate the exponentiation inside-out:

# b ** c → 2 ** 3 → 8

# Then use that result for the outer exponentiation:

# a ** (result from step 1) → 2 ** 8 → 256