# What is the expected output of the following code?
x = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]

def func(data):
    res = data[0][0]
    for da in data:
        for d in da:
            if res < d:
                res = d
    return res

print(func(x[0]))


# Understanding the Data Structure
# The variable x is a 3-dimensional list:

# Outer list has 2 elements

# Each of those has 2 sub-elements

# Each sub-element is a list of 2 numbers

# Visually:

# [
#     [ [1, 2], [3, 4] ],  # x[0]
#     [ [5, 6], [7, 8] ]   # x[1]
# ]
# The Function func(data)
# This function:

# Initializes res with data[0][0] (the first element of the first sublist)

# Iterates through all elements in data (outer loop)

# For each element in data, iterates through its sub-elements (inner loop)

# Updates res whenever it finds a larger value

# Returns the largest value found (res)

# What Happens When We Call func(x[0])
# x[0] is [[1, 2], [3, 4]]

# Let's step through the function:

# res = data[0][0] = 1 (first element of first sublist)

# Outer loop: da takes values [1, 2] and [3, 4]

# First iteration (da = [1, 2]):

# Inner loop compares with 1 and 2

# res becomes 2 (since 1 < 2)

# Second iteration (da = [3, 4]):

# Inner loop compares with 3 and 4

# res becomes 3 (since 2 < 3)

# Then res becomes 4 (since 3 < 4)

# Final res value is 4

# Why the Answer is A (4)
# The function finds the maximum value in the 2D list passed to it (x[0]), which is 4.