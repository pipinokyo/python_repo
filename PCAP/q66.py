# Which of the following expressions evaluates to True and raises no exception?
'''
A.  1  |  10 != '1' + '0'
B.  1  |  'Al' * 2 != 2 * 'Al'
C.  1  |   9' * 3 > '9' * 9
D.  1  |  '9' * 1 < 1 * 2 
'''

# Key Observations:
# | (Bitwise OR) has higher precedence than !=, >, <, so expressions are evaluated as:

# (1 | 10) != '1' + '0' (for Option A)

# (1 | 'Al' * 2) != 2 * 'Al' (for Option B), etc.

# Bitwise OR (|) requires integers (or objects implementing __or__). If a non-integer is used, Python raises TypeError.

# Option A: 1 | 10 != '1' + '0'
# 1 | 10 → Bitwise OR of 1 (0b0001) and 10 (0b1010) → 0b1011 (decimal 11).

# '1' + '0' → String concatenation → '10'.

# 11 != '10' → True (int vs. str, always unequal).

# Result: True (no exception).

# Option B: 1 | 'Al' * 2 != 2 * 'Al'
# 'Al' * 2 → 'AlAl' (string).

# 1 | 'AlAl' → Error! Bitwise OR cannot work with strings.

# Result: TypeError (exception raised).

# Option C: 1 | '9' * 3 > '9' * 9
# '9' * 3 → '999' (string).

# 1 | '999' → Error! Bitwise OR cannot work with strings.

# Result: TypeError (exception raised).

# Option D: 1 | '9' * 1 < 1 * 2
# '9' * 1 → '9' (string).

# 1 | '9' → Error! Bitwise OR cannot work with strings.

# Result: TypeError (exception raised).