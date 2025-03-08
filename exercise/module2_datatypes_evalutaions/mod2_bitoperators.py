# This is used very, very rarely.
# You may work with Python for many years and never use bitwise operators.

# The six operators are Ampersand Bar, Tilde Caret, left shift and right shift.
# & , | , ~ , ^ , << , >>

# & (LOGICAL AND)
# firstbit              0  0  1  1    
# secondbt              0  1  0  1
# firstbit & secondbit  0  0  0  1


# | (LOGICAL OR)
# firstbit              0  0  1  1    
# secondbt              0  1  0  1
# firstbit | secondbit  0  1  1  1


# ^ (LOGICAL XOR)
# firstbit              0  0  1  1    
# secondbt              0  1  0  1
# firstbit ^ secondbit  0  1  1  0


# ~ (LOGICAL NOT)  ~X = -X -1
# ~1 = -2
# ~0 = -1


# shift operators --- the left shift and the right shift.
# <<  left shift operator works like multiplying your decimal number by two to a certain power.
# 12 << 1 = 24 Left shift by one bit means multiply the number by two 
# 12 << 2 = 48 Left shift by two bits means multiply the number by four.
# 12 << 3 = 96 Left shift by three bits means multiply the number by eight.

# >>  Right shift means dividing the number by two To a certain power.
# 12 >> 1 = 6 Right shift by a single bit means divide by two
# 12 >> 2 = 3 Right shift by two bits means divide by four.
#             Right shift by three bits means divide by eight and so on.