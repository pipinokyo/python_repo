# Tuples are a bit similar to lists.
# They are also collections of multiple elements
# all the elements can have the same or different data types
# but tuples are immutable, meaning they cannot be changed after they are created.
# Tuples are defined by enclosing the elements in parentheses () instead of square brackets [].

empty_tuple = ()

one_el_tuple_a = (1,)
one_el_tuple_b = 1,

three_el_tuple = 1, 2, 3

# When you first create a tuple, it stays this way forever.
# You cannot add, remove, or change any of its elements.
# This is what makes tuples immutable.
# You could of course assign a new tuple to the same variable.

user_data = ('Ivan', 'Ivanov', 25) # we start with a tuple like this
user_data = ('cnyt', 'kate', 30) # now we have a new tuple assigned to the same variable
# but the old tuple is still there, it just doesn't have a name anymore

# .append() and .extend() methods do not work with tuples.
# but you cannot use indexing to change individual elements.

print(user_data[0]) # this will print the first element of the tuple
# the output of the above code will be:
# cnyt

user_data[0] = 'new_name' # this will result in an error:

del three_el_tuple_a # this will delete the tuple