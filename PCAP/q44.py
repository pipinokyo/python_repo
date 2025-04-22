# What is the expected output of the following code?

plane = "Cessna"
counter = 0
for c in plane * 2:
    if c in ["e", "a"]:
        counter += 1
print(counter)



# Step-by-Step Execution:
# plane = "Cessna"
# Assigns the string "Cessna" to the variable plane.

# plane * 2

# This performs string repetition: "Cessna" * 2 → "CessnaCessna"
# The resulting string is: 'C' 'e' 's' 's' 'n' 'a' 'C' 'e' 's' 's' 'n' 'a'

# for c in plane * 2:

# This loops through each character in "CessnaCessna".

# if c in ["e", "a"]:

# Checks if the current character c is either 'e' or 'a'.

# If true, increments counter by 1.

# Characters being checked and counter updates:

# Character (c)	Is c in ["e", "a"]?	 counter value
#     'C' 	        No	                    0
#     'e'	            Yes (+1)	            1
#     's'	            No	                    1
#     's'	            No	                    1
#     'n'	            No	                    1
#     'a'	            Yes (+1)	            2
#     'C'	            No	                    2
#     'e' 	        Yes (+1)	            3
#     's'	            No	                    3
#     's'	            No	                    3
#     'n' 	        No	                    3
#     'a'	            Yes (+1)	            4
# print(counter)

# After the loop completes, counter = 4 is printed.

# Visualization:
# "Cessna" * 2 → "CessnaCessna"
# Characters: C, e, s, s, n, a, C, e, s, s, n, a

# Matching characters (e or a):
# 1. 'e' → counter = 1
# 2. 'a' → counter = 2
# 3. 'e' → counter = 3
# 4. 'a' → counter = 4
# Final Output:
# The code will output: 4