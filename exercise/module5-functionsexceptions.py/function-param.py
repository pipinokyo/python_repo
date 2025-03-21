# Let's say that we need to find the average from multiple numbers in a list.
# So we can write the following code.

input_numbers = [5.0, 3.5, 7.8, 9.9, 10.0]

sum = 0.0
for number in input_numbers:
    sum += number
average = sum / len(input_numbers)

print(average)
# the output will be 7.84
# But what if we need to find the average from multiple lists of numbers?
# We would have to repeat the same code for each list, which is not efficient.
# Instead, we can define a function that takes a list of numbers as an argument and returns the average.

input_numbers = [5.0, 3.5, 7.8, 9.9, 10.0]

def get_average(input_numbers):
  sum = 0.0
  for number in input_numbers:
      sum += number
  average = sum / len(input_numbers)
  print(average)
get_average([5.0, 3.5, 7.8, 9.9, 10.0])
# the output will be 7.84
# Now we can call this function with any list of numbers, and it will return the average.


def print_letter_count(text, letter):
  counter = 0
  for char in text:
    if char == letter:
      counter += 1
  print('Number of', letter,  'is', counter)

print_letter_count('Welcome', 'e')
# the output will be 2

print_letter_count('People say nothing is impossible, but I do nothing every day.', 'a')   
# the output will be 2

print_letter_count('e', 'Welcome')
# the output will be 0

print_letter_count(text='Welcome', letter='e')
# the output will be 2
# we can also use keyword arguments to specify the order of the arguments
# this allows us to pass the arguments in any order
# for example, we can call the function like this:
print_letter_count(letter='e', text='Welcome')
# the output will be 2