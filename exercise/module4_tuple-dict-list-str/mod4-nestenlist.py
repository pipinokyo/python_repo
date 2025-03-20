# Lists in general are collections of multiple elements.
numbers = [1, 2, 3, 4] # Each element in this list is an integer.

countries = ['UK', 'US', 'Germany'] # Each element in this list is a string.

countries = [1, 'UK', 2 , 'US'] # Each element in this list can be of different data types.
# Note, however, that this is not recommended and you should avoid it.All the elements of a list should have the same data type.

#  lists can also have other lists as elements.
cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
# This outer list named cells contains two elements inside.

#  if you want to access the first element with index zero, you'll see that you get a sub list in return.
print(cells[0]) # ['A1', 'A2', 'A3']
# if you want to access a specific element in this sublist, all you have to do is add another index.
print(cells[0][1]) # 'A2'
print(cells[0][0]) # 'A1'
print(cells[1][2]) # 'B3'

# let's see what happens when we use a for loop to iterate the list and print its elements.
cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
for x in cells:
    print('Element: ', x)

#  the output will be:
# Element:  ['A1', 'A2', 'A3']
# Element:  ['B1', 'B2', 'B3']

# What if we want to get access to a one, a two, and so on individually?
#  In this case we need to use nested for loops.
cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
for x in cells:
    for y in x:
        print('Element: ', y)
#  the output will be:
# Element:  A1
# Element:  A2
# Element:  A3
# Element:  B1
# Element:  B2
# Element:  B3


# let's say that we want to create a list to represent the following table.
# [1, 2, 3, 4, 5]
# [1, 2, 3, 4, 5]
# [1, 2, 3, 4, 5]
# [1, 2, 3, 4, 5]

# How to initialize a list like this using list comprehension.
#  We can use nested list comprehension.
table = [[i for i in range(1, 6)] for j in range(4)]
print(table)
