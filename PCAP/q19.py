# What is the expected behavior of the following snippet?
s = 'SPAM'
def f(x):
    return s + 'MAPS'
print(f(s))

# Step-by-Step Execution:
# Line 1:

# A variable s is assigned the string value 'SPAM'.

# State: s = 'SPAM'

# Line 2-3:

# A function f is defined with one parameter x.

# Inside the function, s (the global variable) is concatenated with 'MAPS'.

# Note: The parameter x is not used in the function.

# Function definition: f(x) -> returns s + 'MAPS'

# Line 4:

# The function f is called with s (which is 'SPAM') as an argument.

# Since s is a global variable, the function ignores the passed argument x and instead uses the global s.

# The function returns 'SPAM' + 'MAPS' = 'SPAMMAPS'.

# print(f(s)) outputs 'SPAMMAPS'.