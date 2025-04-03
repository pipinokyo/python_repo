# How many stars (*) will the following snippet send to the console?
lst = [[c for c in range(r)] for r in range(3)]
for x in lst:
    for y in x:
        if y < 2:
            print('*', end="")

# 1. List Comprehension Breakdown

# The first line creates a nested list using list comprehension:
# lst = [[c for c in range(r)] for r in range(3)]

# Let's expand this:
# The outer loop for r in range(3) iterates over r = 0, 1, 2.
# For each r, the inner list comprehension [c for c in range(r)] creates a list of numbers from 0 to r-1.
# So, the nested list lst is constructed as follows:

# When r = 0: range(0) is empty → []
# When r = 1: range(1) is [0] → [0]
# When r = 2: range(2) is [0, 1] → [0, 1]
# Thus, lst = [[], [0], [0, 1]].

# 2. Nested Loops and Printing Stars
# Now, let's analyze the nested loops:

# for x in lst:          # x iterates over each sublist in lst
#     for y in x:        # y iterates over each element in x
#         if y < 2:     # if y is less than 2, print a star
#             print('*', end="")

# Let's go through each iteration:
# Outer Loop (for x in lst):
# x = [] (first sublist in lst):
# Inner loop for y in x has no elements (empty list), so nothing happens.
# Stars printed: 0
# x = [0] (second sublist in lst):
# Inner loop:
# y = 0: 0 < 2 is True → print *.
# Stars printed: 1
# x = [0, 1] (third sublist in lst):
# Inner loop:
# y = 0: 0 < 2 is True → print *.
# y = 1: 1 < 2 is True → print *.
# Stars printed: 2

# 3. Total Stars Printed
# Add up the stars from each iteration:
# 0 (first sublist) + 1 (second sublist) + 2 (third sublist) = 3 stars.
# 4. Final Output
# The console will display:
# (3 stars in total, printed consecutively due to end="" in the print statement).