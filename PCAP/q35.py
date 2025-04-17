# What is the expected output of the following code?

def func(num):
    res = '*'
    for _ in range(num):
        res += res
    return res

for x in func(2):
    print(x, end='')


# Step-by-Step Execution
# 1. Function Definition (func)
# The function func takes one parameter num

# Initializes res with the string '*' (single asterisk)

# 2. Calling func(2)
# When we call func(2), here's what happens:

# First Iteration (num = 2, _ = 0):
# Current res: '*'

# Operation: res += res → '*' + '*' → '**'

# New res: '**'

# Second Iteration (num = 2, _ = 1):
# Current res: '**'

# Operation: res += res → '**' + '**' → '****'

# New res: '****'

# After 2 iterations, the function returns '****'

# 3. The Loop for x in func(2):
# func(2) returns '****'

# The loop iterates over each character in this string

# There are 4 characters ('*', '*', '*', '*')

# 4. Printing
# Each '*' is printed with end='', which means no newline between them

# The output will be all asterisks concatenated: ****

# Visualization
# func(2) execution:
# Initialize: res = '*'
# 1st iteration:
# res = '*' + '*' → '**'
# 2nd iteration:
# res = '**' + '**' → '****'
# Final string: '****'
# Loop prints each character:
# 1st: '*' → output: '*'
# 2nd: '*' → output: '**'
# 3rd: '*' → output: '***'
# 4th: '*' → output: '****'
# Final Output
# The expected output of this code is: ****