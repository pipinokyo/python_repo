# What is the expected output of the following snippet?
s = 'python'
for i in range(len(s)):
    i = s[i].upper()
print(s, end="")

# Explanation:
# Initialization:
# s = 'python' assigns the string 'python' to the variable s.
# The string 'python' has 6 characters, indexed as follows:

# s[0] = 'p'
# s[1] = 'y'
# s[2] = 't'
# s[3] = 'h'
# s[4] = 'o'
# s[5] = 'n'

# Loop Execution:
# for i in range(len(s)): iterates over the indices of s (i.e., i takes values 0, 1, 2, 3, 4, 5).

# Inside the loop:
# i = s[i].upper() does two things:
# s[i].upper() converts the character at index i to uppercase (e.g., s[0].upper() gives 'P').
# The result is assigned back to the loop variable i. This does not modify the original string s; it just reassigns the loop variable i to the uppercase character (which has no effect on the string or future iterations).

# Key Observations:
# The original string s is never modified in the loop. The line i = s[i].upper() only changes the loop variable i (which gets overwritten in the next iteration anyway).
# The loop runs 6 times, but it does not alter s in any way.

# Final Output:
# After the loop completes, print(s, end="") prints the original string 'python' (unchanged) with no trailing newline (due to end="").

# Step-by-Step Execution:
# Initialize s = 'python'

# Start loop with i from 0 to 5:
# Iteration 1 (i = 0): i = 'P' (but s remains 'python').
# Iteration 2 (i = 1): i = 'Y' (but s remains 'python').
# Iteration 3 (i = 2): i = 'T' (but s remains 'python').
# Iteration 4 (i = 3): i = 'H' (but s remains 'python').
# Iteration 5 (i = 4): i = 'O' (but s remains 'python').
# Iteration 6 (i = 5): i = 'N' (but s remains 'python').

# After the loop, print s (which is still 'python').

# Final Output:
# python