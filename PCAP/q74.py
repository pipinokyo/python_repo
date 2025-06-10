# What is the expected output of the following code?

x = """
"""

print(len(x))


# Understanding the String Assignment:
# The string x is defined using triple quotes ("""). In Python, triple quotes are typically used for:

# Multi-line strings
# Strings that contain both single and double quotes
# In this case, the string is defined as:
# Opening triple quotes """
# Followed immediately by a newline
# Closing triple quotes """

# What does the string contain?
# The string x consists of:
# The opening """
# A newline character (\n) - because we go to the next line
# The closing """
# However, in Python, the content of a triple-quoted string is what appears between the opening and closing quotes. Here, there's nothing between them except a newline.

# Key Observations:
# The string starts with """ and ends with """ on the next line.
# The only character between them is a newline (\n).
# Therefore, the string x contains a single newline character: "\n".

# Length of the String:
# "\n" is a single character (the newline character).
# Thus, len(x) will return 1.