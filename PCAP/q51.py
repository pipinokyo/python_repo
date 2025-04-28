# What would you insert instead ??? so that the program checks for even numbers?


if ???:
      print('x is an even number')

A.   x % 1 ==  2
B.   x % ‘even’ ==  True 
C.   x % x ==  0
D.   x % 2 ==  0
E.   x % 2 ==  1



# D. x % 2 == 0

# Explanation:
# The modulo operator (%) gives the remainder of a division.

# If a number x is even, dividing it by 2 leaves no remainder (i.e., x % 2 == 0).

# If it’s odd, x % 2 would be 1.

# Why the Other Options Are Wrong:
# A. x % 1 == 2 → Any number divided by 1 has a remainder of 0, so this is always false.

# B. x % ‘even’ == True → Modulo with a string ('even') is invalid (TypeError).

# C. x % x == 0 → This is only true if x != 0 (but doesn’t check for even numbers).

# E. x % 2 == 1 → This checks for odd numbers, not even.

# Correct Code:
# if x % 2 == 0:  
#     print('x is an even number')  
# Example:

# If x = 4, 4 % 2 is 0 → prints "x is an even number".

# If x = 5, 5 % 2 is 1 → nothing happens.