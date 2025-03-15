# Task 4
# You are given two dictionaries where the keys represent item names and the values represent their respective counts
# Input: 
# dict1 = {"apple": 3, "banana": 5, "orange": 2}
# dict2 = {"banana": 2, "orange": 4, "grape": 6}



# Output: 
# {
#     "apple": 3,   # Only in dict1
#     "banana": 7,  # 5 (from dict1) + 2 (from dict2)
#     "orange": 6,  # 2 (from dict1) + 4 (from dict2)
#     "grape": 6    # Only in dict2
# }

# dict1 = {"apple": 3, "banana": 5, "orange": 2}
# dict2 = {"banana": 2, "orange": 4, "grape": 6}

# new_inp = {}                      # this dict will store the combined results from dict1 and dict2

# for key, value in dict1.items():  # The items() method returns a view of key-value pairs in dict1.
#         new_inp[key] = value      # The loop iterates through each key-value pair in dict1 and adds them to new_inp.
#                                   # After this step, new_inp becomes {"apple": 3, "banana": 5, "orange": 2}.
# for key, value in dict2.items():  # The loop iterates through each key-value pair in dict2.
#     if key in new_inp:            # If the key already exists in new_inp,
#        new_inp[key] += value      # the value from dict2 is added to the existing value in new_inp.
#     else:
#        new_inp[key] = value       # If the key does not exist in new_inp, the key-value pair is added to new_inp.

# print(new_inp)


# task 4 alternative way 
dict1 = {"apple": 3, "banana": 5, "orange": 2}
dict2 = {"banana": 2, "orange": 4, "grape": 6}

# Merge and sum counts using a dictionary comprehension
result = {
    key: dict1.get(key, 0) + dict2.get(key, 0)
    for key in set(dict1) | set(dict2)
}
# check this one understand the details
print(result)