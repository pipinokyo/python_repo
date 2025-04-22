# What is the expected output of the following code?

import math

result = math.e != math.pow(2, 4)
print(int(result))


# import math:
# This imports Python's math module, which provides mathematical functions and constants.
# math.e:
# This is the mathematical constant Euler's number (e), approximately 2.71828.

# math.pow(2, 4):
# This calculates 2 raised to the power of 4 (i.e., 2 * 2 * 2 * 2), which equals 16.

# math.e != math.pow(2, 4):

# This checks if math.e (≈2.71828) is not equal to math.pow(2, 4) (16).

# Since 2.71828 ≠ 16, the comparison evaluates to True.

# int(result):

# Converts the boolean True to an integer (1).

# (In Python, int(True) = 1 and int(False) = 0).

# print(int(result)):

# Prints 1 (the integer equivalent of True).

# Visualization:
# math.e       ≈ 2.71828
# math.pow(2, 4) = 16

# Is 2.71828 != 16?   → True

# int(True) → 1
# Output: 1