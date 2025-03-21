print('Hello', 'How are you?', end='.', sep='-')
# # this will print 'Hello-How are you?.'
# # we can also pass arguments to the function 


# let's see how keyword arguments work when you create your own functions.
def print_letter_count(text, letter='a'):
  counter = 0
  for char in text:
    if char == letter:
      counter += 1
  print('Number of', letter,  'is', counter)   
print_letter_count('Welcome')  # the output will be 0
print_letter_count('Welcome', 'e')  # the output will be 2