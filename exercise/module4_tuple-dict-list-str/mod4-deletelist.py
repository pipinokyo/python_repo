top_cities = ['New York', 'Los Angeles', 'Singapore', 'Chicago', 'Houston', 'Phoenix']
# You can see that there is an element at index to Singapore which should actually not be there.
# We type del and we provide the element or elements we want to get rid of.

del top_cities[2] # this will remove the element at index 2 which is Singapore 
# Now we can print the list again to see if Singapore has been removed
print(top_cities) # this will return ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']

# If you now access top cities two, you will see that it points to a new element.
top_cities[2] # this will return 'Chicago' instead of 'Singapore'

# we want to keep the first three elements in the list and we want to delete the remaining
# We can use the Del Instruction alongside slicing to do that in a single operation.
del top_cities[3:] # this will remove all elements starting from index 3 until the end of the list
# Now we can print the list again to see if the last two elements have been removed
print(top_cities) # this will return ['New York', 'Los Angeles', 'Chicago']

# You can also delete all elements from a list using a slice with both indices omitted.
del top_cities[:] # this will remove all elements from the list
# Now we can print the list again to see if all elements have been removed
print(top_cities) # this will return an empty list []
# Note that the list still exists, but it is now empty.

# You can also delete the entire list using the del instruction.
del top_cities # this will remove the list entirely
# If you now try to print the list, you will get an error because the list no longer exists.
# print(top_cities) # this will return an error because the list no longer exists