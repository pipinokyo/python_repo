# What is the expected output of the following snippet?
dict = { 'a': 1, 'b': 2, 'c': 3 }
for item in dict:
    print(item)

# Explanation:
# Dictionary Creation:
# The dictionary dict is created with three key-value pairs:

# 'a': 1
# 'b': 2
# 'c': 3

# Iterating Over the Dictionary:
# When you loop over a dictionary directly using for item in dict, the loop iterates over the keys of the dictionary by default.
# So, in each iteration, item will be assigned one of the keys of the dictionary.

# Order of Iteration:
# In modern Python (Python 3.7+), dictionaries preserve the insertion order by default. This means the keys will be iterated in the order they were added to the dictionary unless the dictionary is modified.
# Here, the order of insertion is 'a', 'b', then 'c'.

# Output:
# In each iteration, the current key is printed.
# Thus, the output will be:

# a
# b
# c