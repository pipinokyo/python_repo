for char in 'happy message':
  print(char)
# The operator indicates that the for loop should check every element in the happy message string.
# However, the in operator can also be used to check whether a given element is present in a list.

# Take a look at the following code.

invited_guests = ['kate', 'adam', 'kerry', 'joe', 'anne', 'marie']
name = input('What is your name? ')
if name in invited_guests:
  print('You are invited!')
else:
  print('You are not invited.')

# The Simple program has a predefined list of invited guests.
# It then asks the user for their name and checks if the user's name is in the list.
# If the user's name is in the list, we print a welcome message.
# Otherwise, we inform the user that they are not invited.

# the output of the code will be
# What is your name? kate
# You are invited!
# What is your name? john
# You are not invited.

# We can also use a negated in operator, not in.
# Take a look at the following code.
invited_guests = ['kate', 'adam', 'kerry', 'joe', 'anne', 'marie']
name = input('What is your name? ')
if name not in invited_guests:
  print('You are not invited!')
else:
  print('You are invited.')
# The Simple program has a predefined list of invited guests.
# It then asks the user for their name and checks if the user's name is not in the list.
# If the user's name is not in the list, we print a message that they are not invited.
# Otherwise, we inform the user that they are invited.
# the output of the code will be
# What is your name? john
# You are not invited!
# What is your name? kate
# You are invited.