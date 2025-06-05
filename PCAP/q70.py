# What is the expected output of the following code?

print(list('hello'))

# Step-by-Step Breakdown:

# 'hello' (Input String)
# This is a string literal: 'hello'.
# In Python, strings are iterable sequences of characters.
# list('hello') (Conversion to List)
# The list() function iterates over the string and converts each character into a separate element in a new list.

# Breakdown of iteration:
# 'h' → List element
# 'e' → List element
# 'l' → List element
# 'l' → List element
# 'o' → List element
# Resulting List

# The output is a list of characters:

# python
# ['h', 'e', 'l', 'l', 'o']