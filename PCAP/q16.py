# What is the expected behavior of the following snippet?
x = 5
f = lambda x: 1 + 2
print(f(x))

# Code Breakdown:
# x = 5
# f = lambda x: 1 + 2
# print(f(x))
# Step-by-Step Execution:
# Variable Assignment:

# x = 5 assigns the value 5 to the variable x.

# Lambda Function Definition:

# f = lambda x: 1 + 2 defines a lambda (anonymous) function that:

# Takes a parameter x (but does not use it in the function body).

# Always returns 1 + 2 (which is 3), regardless of the input x.

# Function Call:

# f(x) calls the lambda function f with the argument x (which is 5).

# However, since the lambda ignores its input (x is unused), the result is simply 1 + 2 = 3.

# Output:

# print(f(x)) prints the result of f(x), which is 3.