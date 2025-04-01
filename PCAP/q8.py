# What is the expected output of the following snippet?
lst = ["A", "B", "C", 2, 4]
del lst[0:-2]
print(lst)

# Indices of the list elements:

# 0: "A"
# 1: "B"
# 2: "C"
# 3: 2
# 4: 4

# Slicing in del lst[0:-2]:
# The slice [0:-2] means:
# Start at index 0 (inclusive)
# End at index -2 (exclusive), which refers to the element 2 (since -1 is 4, -2 is 2).
# So, lst[0:-2] selects elements from index 0 up to (but not including) index -2:
# This includes indices 0 ("A"), 1 ("B"), and 2 ("C").
# Effect of del lst[0:-2]:
# The del statement removes the sliced portion (["A", "B", "C"]) from the list.
# The remaining list after deletion is [2, 4].