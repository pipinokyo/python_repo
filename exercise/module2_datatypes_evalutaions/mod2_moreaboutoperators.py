2 + 3 * 2 # Python starts with multiplication. # the answer is 8 here
(2 + 3) * 2 # in this case the answer is 10


# the precision of floating point numbers in Python.
# 0.15625 is a float but in binary is 001111100010000000000000000000000000 goes like this
# your float numbers in Python are stored in memory as very long chains of zeros and ones.
# Because of that, there are some limitations.
# Most floats cannot be represented exactly as binary fractions.
# As a consequence, the floats that you use in Python are only approximated rounded
# when they are stored as binary numbers in your computer.
# In other words, the float numbers are more or less right, but they are not 100% correct.

0.1 + 0.1 + 0.1 = 0.30000000000000004



# the exponentiation operator.
# Take a look at this operation.
2 ** 2 ** 3
#There are two exponentiation operations here to be performed, and the order of operations does matter.
# If we start from the left the answer is 64
# If we start from the right the answer is 256

# python starts from the right in this case so the second option is correct
# the exponentiation operator uses right sided binding, which means it starts from the right.