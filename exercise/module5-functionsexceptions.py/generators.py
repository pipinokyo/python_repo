# interesting type of function in Python that is called generators 
# # generators are a special type of function that can be used to create iterators
# # they are defined using the yield keyword instead of return
# # when a generator function is called, it returns a generator object

# Let's see a simple example.
def get_numbers():
    for i in range(1, 4):
        yield i
# when we call the get_numbers() function, it returns a generator object
# we can use this generator object to iterate over the numbers
print(get_numbers())  # <generator object get_numbers at 0x...>

# We can now ask the generator to provide us with values one by one, using a special instruction.
# This instruction is called next().
# The next() function retrieves the next value from the generator.
numbers = get_numbers()
print(next(numbers))  # 1
print(next(numbers))  # 2
print(next(numbers))  # 3
# If we try to call next() again, it will raise a StopIteration exception
# because there are no more values to yield from the generator.

# You can also use a for loop with a generator in the following way.
for number in get_numbers():
    print(number)  # 1, 2, 3
# The for loop automatically handles the StopIteration exception for us.

# One more thing you can do with generators is turn them into lists using the list function.
numbers_list = list(get_numbers())
print(numbers_list)  # [1, 2, 3]