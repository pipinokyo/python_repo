# Task 3: Find Common Elements in Two Lists
# Write a function that takes two lists as input and returns a list containing only the common elements (without duplicates).
# Example:
# print(common_elements([1, 2, 3, 4], [3, 4, 5, 6]))  
# Output:
# [3, 4]



def two_list(list1, list2): # We define a function named two_list that takes two parameters: list1 and list2 (both are lists).
    common = [] # We create an empty list called common to store the common elements.

    for i in list1: # We use a for loop to iterate through each element in list1.
        if i in list2: # For each element in list1, we check if it exists in list2 using the in operator.
            if i not in common: # If the element is present in both list1 and list2, we check if it is already in the common list.
                common.append(i) # If the element is common and not already in the common list, we add it to the list
    return common # The function returns the common list containing the common elements.

list1 = input('enter the first list of number: ').split()
list2 = input('enter the second list of number: ').split()
# The input() function takes user input as a string.
# The split() method splits the input string into a list of substrings based on spaces.

Result = two_list(list1, list2) # We call the two_list function with list1 and list2 as arguments. The result is stored in the Result variable.
print(Result)
