# Task 2: Remove Duplicates from a List
# Ask the user to enter multiple words separated by spaces. Store them in a list and remove duplicate words while maintaining the original order.
# Example:
# Enter words: apple banana apple cherry banana apple  
# Filtered List: ['apple', 'banana', 'cherry']


# Using a loop: This is a more manual method and can be less efficient for large lists.
list = input('Enter words seperated by spaces: ').split() # # .split() splits the input into as list based on spaces
print("original list: ", list)
filtered_list = []
for i in list: # checks every word in the list
    if i not in filtered_list: # checks if the current word(i) is not already in the filterd_list
        filtered_list.append(i) # Adds the current word (i) to the filtered_list if it is not already present.
print('filetered list: ', filtered_list)


# Using set(): This is the most common and efficient way, especially for large lists, as it leverages the property of sets to only store unique elements. The original order of elements might not be preserved.
list1 = input('Enter words seperated by spaces: ').split()
print("original list: ", list1)
filtered_list = list(set(list1)) # set(list1) converts the list to a set: {'apple', 'banana', 'orange'}.
# list(set(list1)) converts the set back to a list: ['apple', 'banana', 'orange']
print('filtered list: ', filtered_list)
# note that i could not use list here as a variable because list is a built-in function(used to convert other iterables, like sets, into lists).


# Using dict.fromkeys(): This method also preserves the original order of elements
list1 = input('Enter words seperated by spaces: ').split()
print("original list: ", list1)
filtered_list = list(dict.fromkeys(list1))
# dict.fromkeys() is a built-in Python method that creates a dictionary from the given iterable (in this case, list1).
# Dictionaries in Python cannot have duplicate keys, so any duplicate words in list1 are automatically removed.
# list(dict.fromkeys(list1)): list function Converts the dictionary keys back into a list.
print('filtered list: ', filtered_list)
