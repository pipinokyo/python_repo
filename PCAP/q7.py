# What is the expected output of the following snippet?
s = "Hello, Python!"
print(s[-14:15])

# Explanation:
# String Indexing in Python:

# Positive indices start from 0 (left to right).

# Negative indices start from -1 (right to left).

# For the string s = "Hello, Python!", the indices are as follows:

# Character	            H	 e	 l	 l	 o	 ,		 P	 y	 t	h	o	n	!
# Index	                0	 1	 2	 3	 4	 5	 6	 7	 8	 9	10	11	12	13
# Negative Index       -14  -13	-12	-11	-10	-9	-8	-7	-6	-5	-4	-3	-2	-1


# Slicing s[-14:15]:

# The slice s[start:end] extracts characters from start (inclusive) to end (exclusive).
# Here, start = -14 (which refers to the first character 'H').
# end = 15, which is out of bounds (the string only has indices up to 13).
# → Python handles this gracefully and treats it as the end of the string.