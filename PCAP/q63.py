# What is the output of the following code snippet?

def test(x=1, y=2):
    x = x + y
    y += 1
    print(x, y)

test(2, 1)


# Step-by-Step Execution:
# Function Definition:
# test(x=1, y=2) defines a function with:
# Default parameter x=1 (used if no argument is provided)
# Default parameter y=2 (used if no argument is provided)

# Function Call:
# test(2, 1) is called with arguments 2 for x and 1 for y
# This overrides the default values, so inside the function:
# x starts as 2 (passed value)
# y starts as 1 (passed value)
# First Operation (x = x + y):
# x = 2 + 1 → x becomes 3
# Now: x = 3, y = 1

# Second Operation (y += 1):
# y = 1 + 1 → y becomes 2
# Now: x = 3, y = 2

# Print Statement (print(x, y)):

# Prints 3 2 (current values of x and y)