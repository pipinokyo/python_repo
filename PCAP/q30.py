# Which of the following statements are true? (Select two answers)

# A. The first argument of the open() function is an integer value.
# B. The input() function reads data from the stdin stream.
# C. There are three pre-opened file streams.
# D. The readiness() function returns a string.


# The Correct Answers are B and C
# B. The input() function reads data from the stdin stream.
# In Python, input() reads user input from the standard input stream (stdin), which is typically the keyboard.

# Example:

# user_input = input("Enter something: ")  # Reads from stdin (keyboard)
# print("You entered:", user_input)
# C. There are three pre-opened file streams.
# In Unix-like systems (and Python), there are three standard pre-opened file streams:

# stdin (standard input) - for reading input (file descriptor 0)

# stdout (standard output) - for writing output (file descriptor 1)

# stderr (standard error) - for writing errors (file descriptor 2)

# Example:

# import sys
# sys.stdin   # Standard input (keyboard by default)
# sys.stdout  # Standard output (console by default)
# sys.stderr  # Standard error (console by default)
# Why the Other Options are Wrong:
# A. The first argument of the open() function is an integer value.
# False. The first argument of open() is a string representing the file path, not an integer.
# Example:

# file = open("example.txt", "r")  # "example.txt" is a string, not an integer.
# D. The readiness() function returns a string.
# False. There is no built-in readiness() function in Python. This is likely a distractor.

# Summary
# ✅ B is correct because input() reads from stdin.

# ✅ C is correct because there are three pre-opened streams (stdin, stdout, stderr).

# ❌ A is wrong because open() expects a filename (string), not an integer.

# ❌ D is wrong because readiness() is not a valid Python function.

# Final Answer: B, C ✅