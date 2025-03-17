# available logical operators

# < less than
# > greater than
# <= less than or equal
# >+ greater than or equal
# == equal
# != not equal


password = input('do you know the secret password? ')
if password != '--secret':
    print('not correct')
else:
    print('correct password')


# when Python sees a condition with one of the logical operators, it checks whether the condition is met or not.
# The result is always a boolean value.A boolean variable can have one of two values.True or false?
# do not use quotes around the words true and false. If you use quotes, you'll get a string instead of a boolean.
# remember to start the words true and false with capital letters.
# if blocks are only executed when the condition equals true.

examples:

if True:
    print('conditions met') # the output will be conditions met

if False:
    print('conditions met') # it wont work

if 2 == 2:
    print('true') # the output will be true

if 1 == 2:
    print('true') # it won't work

if 2 == 2.0:
    print('true') # Python automatically converts the integer here into a float and 2.0 equals 2.0.