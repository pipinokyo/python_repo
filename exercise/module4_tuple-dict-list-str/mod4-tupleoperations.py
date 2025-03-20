# you can use the Len function to count the number of elements in a tuple.
user_data = ('John', 'American', 1964)
print(len(user_data))
# the output of the above code will be:
# 3

# You can use the in and not in operators the same way as with lists.
user_data = ('John', 'American', 1964)
if 'American' in user_data:
    print('This person comes from the US')
# the output of the above code will be:
# This person comes from the US
if 'Russian' not in user_data:
    print('This person does not come from Russia')

# You can also iterate a tuple with a for loop
user_data = ('John', 'American', 1964)
for item in user_data:
    print(item)
# the output of the above code will be:
# John
# American
# 1964

# Tuples can also be added together or multiplied by an integer.
user_data = ('John', 'American', 1964) + ('teacher', 'male') # in the background, you are creating a new tuple
# by adding two tuples together.
print(user_data)
# the output of the above code will be:
# ('John', 'American', 1964, 'teacher', 'male')

numbers = (0, 1) * 10
print(numbers)
# the output of the above code will be:
(0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1)

