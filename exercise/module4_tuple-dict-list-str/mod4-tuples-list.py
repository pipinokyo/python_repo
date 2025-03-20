# Python allows you to put lists as tuple elements
# and the other way around to put tuples as list elements.

# We'll start with tuples in lists
# Let's create a tuple that represents some basic information about London, the capital of UK.
city_1 = ('London', 'UK', 8.98)

# Now let's create a similar tuple with some basic info about Canberra, the capital of Australia.
city_2 = ('Canberra', 'Australia', 0.4)

# And finally, let's add some info about Algiers, the capital of Algeria.
city_1 = ('Algeirs', 'Algeria', 3.9)

# We've got three separate variables with three separate cities,
# so it perhaps makes sense to have them in a single list 
capitals = [('London', 'UK', 8.98), ('Canberra', 'Australia', 0.4), ('Algeirs', 'Algeria', 3.9)]

# Each of the elements is a tuple and we can work with such lists the usual way.
for capital in capitals:
    print(capital)

# The output of the above code will be:
# ('London', 'UK', 8.98)
# ('Canberra', 'Australia', 0.4)
# ('Algeirs', 'Algeria', 3.9)
# Now let's say we want to print the name of each capital city.
for capital in capitals:
    print(capital[0])
# The output of the above code will be:
# London
# Canberra
# Algeirs

for capital in capitals:
        print('name:', capital[0], 'country:', capital[1], 'population:', capital[2])
# The output of the above code will be:
# name: London country: UK population: 8.98
# name: Canberra country: Australia population: 0.4
# name: Algeirs country: Algeria population: 3.9


# Now, how about lists in tuples?
# Let's say we have a user tuple with some basic user data.

user_data = ('John', 'American', 1964, [77.0, 78.4, 76.9])
# So here you have an interesting example of a list inside a tuple.

# Even though the tuple itself is immutable and you can't add new elements to the tuple
# the tuples last element, which is a list, is still mutable, so you can't add another list to the tuple.
#  You can't get rid of an existing element of the tuple
# but you can change the contents of the list.  
user_data[3].append(80.9)
print(user_data)
# The output of the above code will be:
# ('John', 'American', 1964, [77.0, 78.4, 76.9, 80.9])
# So you can see that the list inside the tuple is mutable, but the tuple itself is immutable.