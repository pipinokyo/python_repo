# What is the expected output of the following code?

list1 = [1, 3]
list2 = list1
list1[0] = 4
print(list2)


# Explanation with Visualization:
# Initial Assignment:

# list1 = [1, 3]
# This creates a list object [1, 3] in memory, and list1 refers to it.

# list1 --> [1, 3]
# Assigning list2 = list1:

# list2 = list1
# This does not create a new list. Instead, list2 now refers to the same list object as list1.

# list1 --> [1, 3] <-- list2
# Modifying list1[0] = 4:

# list1[0] = 4
# Since list1 and list2 point to the same list, modifying an element via list1 also affects list2.

# list1 --> [4, 3] <-- list2
# Printing list2:

# print(list2)
# Since list2 refers to the same modified list, the output is [4, 3].

# Key Concept:
# In Python, lists are mutable objects, and assigning list2 = list1 makes both variables reference the same object in memory (not a copy). This is called aliasing.
# Changes made through one variable will be reflected in the other because they point to the same underlying list.