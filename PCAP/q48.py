# What is the expected output of the following code?

file = open('data.txt', 'w+')
print('Name of the file: ', file.name)

s = 'Peter Wellert\nHello everybody'
file.write(s)
file.seek(0)
for line in file:
    print(line)

file.close()

# 1. Opening the File (open())
# file = open('data.txt', 'w+')
# Mode 'w+': Opens the file for writing + reading.

# If data.txt doesn’t exist, it creates it.

# If it exists, it truncates (erases) it before writing.

# file.name: Stores the filename ('data.txt').

# Visualization (After Opening)
# File: data.txt
# Status: Empty (truncated if it existed)
# File pointer: Position 0 (start of file)
# 2. Writing to the File (write())
# s = 'Peter Wellert\nHello everybody'
# file.write(s)
# Writes the string s into data.txt.

# \n creates a new line → "Peter Wellert" (Line 1) and "Hello everybody" (Line 2).

# Visualization (After Writing)
# File: data.txt
# Content:
# 1| Peter Wellert
# 2| Hello everybody
# File pointer: At the end (position 28)
# 3. Resetting the File Pointer (seek(0))

# file.seek(0)
# Moves the file pointer back to the start (position 0) so we can read from the beginning.

# Visualization (After seek(0))
# File pointer: Back to position 0 (start)
# 4. Reading the File Line by Line (for line in file)

# for line in file:
#     print(line)
# Iterates through each line in data.txt.

# Since \n splits the content, it reads:

# "Peter Wellert\n" (Line 1)

# "Hello everybody" (Line 2)

# Output (Printed Lines)
# Peter Wellert

# Hello everybody
# Note: print(line) adds an extra newline (since each line already ends with \n).

# 5. Closing the File (close())
# file.close()
# Releases system resources.

# Best practice: Use with open() as file: (auto-closes file).

# Final File State
# data.txt Contents:
# Peter Wellert
# Hello everybody