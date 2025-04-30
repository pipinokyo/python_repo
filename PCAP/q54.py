# What is the expected output of the following code?

foo = [i + i for i in range(5)]
print(foo)


# Understanding the Code
# List Comprehension: [i + i for i in range(5)]

# This is a list comprehension, a concise way to create lists in Python.

# The general structure is:
# [expression for item in iterable]

# Here, the expression is i + i, the item is i, and the iterable is range(5).

# range(5):

# range(5) generates numbers from 0 to 4 (inclusive), i.e., [0, 1, 2, 3, 4].

# Expression i + i:

# For each i in range(5), the expression i + i computes the sum of i with itself (equivalent to 2 * i).

# Resulting List:

# The list comprehension evaluates i + i for each i in range(5) and collects the results into a new list.

# Step-by-Step Evaluation
# Let's break down how the list is constructed:

# Iteration	i (from range(5))	i + i	Result
#     1	            0	        0 + 0	  0
#     2               1	        1 + 1	  2
#     3	            2	        2 + 2     4
#     4           	3	        3 + 3	  6
#     5           	4	        4 + 4	  8
# So, the resulting list foo will be [0, 2, 4, 6, 8].