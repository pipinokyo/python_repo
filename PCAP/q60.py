# Assuming that the open() invocation has gone successfully, the following snippet will:

for x in open('file', 'rt'):
    print(x)


# Step-by-Step Execution:
# File Opening:

# open('file', 'rt') opens a file named 'file' in the current directory
# 'rt' means:
# 'r' - open for reading (default mode)
# 't' - text mode (default mode)
# This returns a file object that is iterable

# Iteration:
# The for loop iterates over the file object line by line
# In each iteration:
# x gets assigned the next line from the file
# The line includes the newline character (\n) at the end

# Printing:
# print(x) prints the current line
# Since x already contains a newline, and print() adds another newline by default, this would result in double-spaced output

# Visualization:
# If 'file' contains:

# Line 1
# Line 2
# Line 3
# The execution would be:

# First iteration:
# x = "Line 1\n"
# print(x) → outputs "Line 1" followed by two newlines

# Second iteration:
# x = "Line 2\n"
# print(x) → outputs "Line 2" followed by two newlines

# Third iteration:
# x = "Line 3\n"
# print(x) → outputs "Line 3" followed by two newlines

# Output:
# The actual output would look like this (with blank lines between):

# Line 1

# Line 2

# Line 3