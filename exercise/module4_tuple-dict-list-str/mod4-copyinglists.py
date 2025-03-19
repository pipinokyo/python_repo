# we'll explain how to copy a list into a new variable.
# This might seem easy, but there is a catch that we need to discuss.

name_original = 'jon snow'
name_new = name_original
name_original = 'Daenerys Targaryen'
print(name_original , name_new)
# the output of the code will be
# Daenerys Targaryen jon snow
# The important thing here is that the name, original and name new have the same value, but they are independent of each other.


list_original = [1,2,3]
list_new = list_original
list_original[0] = -5
print('Original:', list_original , '\nNew', list_new)
# the output of the code will be
# Original: [-5, 2, 3]
# new [-5, 2, 3]
# Look what happened here.
# We tried to copy the content of the original list into the new list.
# But when we later modify the original list, the new list is also modified.
# Both variables now point to the very same place in the memory with the very same list.


# how can you actually make a copy of a list so that two variables have two separate lists that you can modify independently
# In Python, all you have to do is use slicing.
list_original = [1,2,3]
list_new = list_original[:]
list_original[0] = -5
print('Original:', list_original , '\nNew', list_new)
# the output of the code will be
# Original: [-5, 2, 3]
# New: [1, 2, 3]

# Look how similar both versions of the code are.
# All we had to do is add slicing from the very beginning to the very end of the list.

# Naturally, you can also copy a selected fragment of the original list using slicing.
# If you want to copy the first two elements into a new list.
list_original = [1,2,3]
list_new = list_original[:2]
list_original[0] = -5
print('Original:', list_original , '\nNew', list_new)
# the output of the code will be
# Original: [-5, 2, 3]
# New: [1, 2]
