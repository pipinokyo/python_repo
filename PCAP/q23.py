# What is the expected output of the following code?
x = [0, 1, 2]      # Line 1
x.insert(0, 1)     # Line 2
del x[1]           # Line 3 
print(sum(x))      # Line 4


# Step-by-Step Execution

# Line 1: Initial List Creation
# x = [0, 1, 2]
# Visualization:
# Index: 0 1 2
# Value:0 1 2

# Line 2: Insert Operation
# python
# Copy
# x.insert(0, 1)
# This inserts the value 1 at index 0 (the beginning of the list).

# Visualization after insert:
# Before insert: [0, 1, 2]
# After insert:  [1, 0, 1, 2]
# New indexes:
# Index: 0 1 2 3
# Value:1 0 1 2

# Line 3: Delete Operation

# del x[1]
# This deletes the element at index 1 (which is 0 in our current list).

# Visualization:
# Before delete: [1, 0, 1, 2]
# Delete index 1 (value 0)
# After delete:  [1, 1, 2]
# New indexes:

# Index: 0 1 2
# Value:1 1 2
# Line 4: Sum Calculation
# print(sum(x))
# Now we sum the remaining elements: 1 + 1 + 2 = 4