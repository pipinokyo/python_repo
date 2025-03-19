# Lists are usually used to store multiple values of the same type
# multiple integers, multiple floats or multiple strings.

# let's say we want to keep the names of the top five most popular cities in the US.
city_1 = 'New York City'
city_2 = 'Los Angeles'
city_3 = 'Chicago'
city_4 = 'Houston'
city_5 = 'Phoenix'
#  Unfortunately, working with multiple variables like this is not easy.


# It's much better to use a single variable with a list inside
empty_list = []

# if you do want some elements inside, you provide them inside the square brackets, separated by commas
top_cities =['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
print(top_cities)
# this is the output of the list
['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']

# List indices start at zero 
# So the first element in the list has the index of zero.
# So the first element in the list has the index of zero.


# indexing the list
top_cities[0]# this will return 'New York City'
top_cities[1]# this will return 'Los Angeles'
top_cities[2]# this will return 'Chicago'
top_cities[5]# this will return an error because there is no sixth element in the list

# you can also use negative indices to count from the end of the list  
top_cities[-1]# this will return 'Phoenix'
top_cities[-2]# this will return 'Houston' 

#  slicing the list
# you can use the colon operator to slice the list
top_cities[0:2]# this will return ['New York City', 'Los Angeles']
# The first index is the first element to include in the slice
# and the second index is the first element to exclude from the slice
# so the slice top_cities[0:2] includes elements 0 and 1, but not 2
top_cities[1:4]# this will return ['Los Angeles', 'Chicago', 'Houston']

top_cities[2:]# this will return ['Chicago', 'Houston', 'Phoenix']
#  this means take all elements starting at index two until the very end of the list.

top_cities[:3]# this will return ['New York City', 'Los Angeles', 'Chicago']
# This in turn means take all elements from the list from the start until the index three exclusive.

top_cities[:] # this will return the entire list
#  this means take all elements from the start until the end of the list.

# you can also use negative indices to slice the list
top_cities[-3:]# this will return ['Chicago', 'Houston', 'Phoenix']
top_cities[:-2]# this will return ['New York City', 'Los Angeles', 'Chicago']


# Note that you never get an error when you try to enter non-existing indices with slicing.
# If you exceed the boundaries, you will simply get an empty list
top_cities[5:]# this will return an empty list []

# Note that when you access a single element, you get a string value.
top_cities[0]# this will return 'New York City'
# But when you slice the list, you get a new list with the sliced values inside it.
top_cities[0:1]# this will return ['New York City']
#  you can also use the built-in function len() to get the length of the list
len(top_cities) # this will return 5    