# strings are also sequences just like lists.
# we can use indexing and slicing with strings to read individual characters or groups of characters.
fav_band = 'Green day'
print(fav_band[6])
# the output of the above code will be:
# d 

print(fav_band[:6])
# the output of the above code will be:
# Green

print(fav_band[6:])
# the output of the above code will be:
# day

# Note, however, that you cannot use indexing to change individual characters within a string.
fav_band[6] = M
# this will result in an error:
# TypeError: 'str' object does not support item assignment
# strings are immutable, meaning they cannot be changed after they are created.

# strings in Python have many built in methods Python.org to see them all.

text = 'please capitilize this sentence'
text_cap = text.upper()
print(text_cap)
# the output of the above code will be:
# PLEASE CAPITILIZE THIS SENTENCE

user_input = input('please provide a number: ')
if user_input.isnumeric():
    print('thank you that\'s a correct number')
else:
    print('sorry,', user_input, 'is not a number')

# the output of the above code will be:
# please provide a number: 123
# thank you that's a correct number
# or
# please provide a number: abc
# sorry, abc is not a number

user_number = input('please enter a number')
if user_number.isdigit():
    print('this is a number')
else:
    print('this is not a number')
# the output of the above code will be:
# please enter a number 123
# this is a number
# or
# please enter a number abc
# this is not a number