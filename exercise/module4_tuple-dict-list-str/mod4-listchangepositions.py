# Our user provides two numbers that we save in two variables named first and second.
first = input('Enter first number: ')
second = input('Enter second number: ')
# we then need to swap the values we want the first variable to have the value of the second variable
# and we want the second variable to have the value of the first variable.
# So now if you try the following.
first = second # Then you have the value of the second variable in the first variable,
# but the other value is lost. first and second now have the same value.
second = first # you end up with two variables having the very same value.

#  check this out
first = input('Enter first number: ')
second = input('Enter second number: ')
print('Before swapping: ', first, second)
first = second
second = first
print('After swapping: ', first, second)

#  the output is will be
# Enter first number: 10
# Enter second number: 20
# Before swapping:  10 20
# After swapping:  20 20
#  this is not what we want. it doesn't work because we lose the value of the first variable when we assign the value of the second variable to it.


# Swapping the values of two variables requires using an additional third variable.
# You save the value of the first variable to the temporary third variable so that you don't lose it.
#  take a look at this
first = input('Enter first number: ')
second = input('Enter second number: ')
print('Before swapping: ', first, second)
temp = first
first = second
second = temp
print('After swapping: ', first, second)

#  the output is will be
# Enter first number: 10
# Enter second number: 20
# Before swapping:  10 20
# After swapping:  20 10
# This method works fine, as you can see, but Python also has a nice shortcut.

#  take a look at this
first = input('Enter first number: ')
second = input('Enter second number: ')
print('Before swapping: ', first, second)
first, second = second, first
print('After swapping: ', first, second)

#  the output is will be
# Enter first number: 10
# Enter second number: 20
# Before swapping:  10 20
# After swapping:  20 10


# you can use the very same logic with list elements.
#  take a look at this
top_cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
print(top_cities)
top_cities[0], top_cities[4] = top_cities[4], top_cities[0]
print(top_cities)

#  the output is will be
['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
['Phoenix', 'Los Angeles', 'Chicago', 'Houston', 'New York']


# We also typically change element positions when we sort list elements.
# Python has dedicated list methods to sort lists alphabetically.
#  take a look at this

top_cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
top_cities.sort()
print(top_cities)

#  the output is will be
# ['Chicago', 'Houston', 'Los Angeles', 'New York', 'Phoenix'] 
#  this is the sorted list in alphabetical order.
#  you can also sort the list in reverse order using the reverse parameter.
top_cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
top_cities.sort(reverse=True)
print(top_cities)
#  the output is will be
# ['Phoenix', 'New York', 'Los Angeles', 'Houston', 'Chicago']

random_numbers = [5, 3, 8, 1, 2]
random_numbers.sort()
print(random_numbers)
#  the output is will be
# [1, 2, 3, 5, 8]


random_numbers = [5, 3, 8, 1, 2]
random_numbers.sort(reverse=True)
print(random_numbers)
#  the output is will be
# [8, 5, 3, 2, 1]

# Note One thing sort used here and here is a method, meaning it changes the list it belongs to.
# Once you use sort, there's no coming back.You can't undo this operation easily.

top_cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
print(sorted(top_cities))
print(top_cities)

#  the output is will be
# ['Chicago', 'Houston', 'Los Angeles', 'New York', 'Phoenix']
# ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
#  Note that the original list remains unchanged.