# and
# user_age = int(input('What is your age? '))
# user_country = input('What is your country? ')

# if user_age < 25 and user_country == 'Germany':
#   print('You can apply for a German student card.')
# else:
#   print('You cannot apply for a German student card.')

# you can add multiple and. in this case both condition should be met not one of them.

# the output 
# What is your age? 22
# What is your country? Germany
# You can applu for a German student card.


# or
# user_country = input('What is your country?')

# if user_country == 'Sweeden' or user_country == 'Denmark' or user_country == 'Norway':
#   print('You can apply for a Scandinavian student student exchange programme.')
# else:
#   print('Sorry, you are not qualify')

# The if look will be executed if at least one of the conditions is met in the case of an or operator,
# Python first evaluates the condition on the left, meaning user country equals Sweden.
# If this condition is true, Python doesn't even look at the condition on the right.

# the output
# What is your country?Sweeden
# You can apply for a Scandinavian student student exchange programme.


# not
# user_country = input('Where do you come from? ')
# if not user_country == 'Germany':
#   print('You are not from Germany')
# else:
#   print('You are from Germany')

# Not negates the boolean value.
# If a condition is true, then it will turn it false and the other way around.

# the output
# Where do you come from? Germany
# You are from Germany


# you can also join all three operators and or and not in the same complex condition
# user_age = int(input('What is your age? '))
# user_country  = input('What is your country? ')

# if not user_country == 'Germany' and user_age < 25 or user_country == 'Germany' and user_age < 23:
#   print('You qualify')
# else:
#   print('You don\'t qualify')

# the output
# What is your age? 26
# What is your country? tuekr
# You don't qualify


# Just like with mathematical operators, Boolean operators have their priorities.
# 1. not
# 2. and
# 3. or