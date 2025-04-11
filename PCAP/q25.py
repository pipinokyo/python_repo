# What is the expected output of the following code?
data = ['Peter', 404, 3.03, 'Wellert', 33.3]
print(data[1:3])

# Visualization
# Let's visualize the list with indices:

# Index:   0       1     2       3        4
# Value: 'Peter', 404, 3.03, 'Wellert', 33.3
# How Slicing Works
# The slice notation data[1:3] means:

# Start at index 1 (inclusive)

# End at index 3 (exclusive)

# So it includes elements at indices 1 and 2

# Step-by-Step Execution
# The list data is created with 5 elements

# When we slice with data[1:3]:

# Index 1: 404

# Index 2: 3.03

# Index 3 is not included (slice is exclusive of the end index)

# The result is a new list containing [404, 3.03]