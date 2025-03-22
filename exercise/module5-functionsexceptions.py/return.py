def get_average(input_numbers):
    sum = 0.0
    for number in input_numbers:
        sum += number
    average = sum / len(input_numbers)
    return average

print('The average is:', get_average([1, 2, 3, 4, 5])) 
# # the output will be 3.0

average = get_average([1, 2, 3, 4, 5])
if average > 3:
  print('The average is greater than 3')
else:
  print('The average is not greater than 3')
# # the output will be 'The average is greater than 3'


def get_average(input_numbers):
  sum =0.0
  for number in input_numbers:
    sum += number
  average = sum / len(input_numbers)
  return average
  print('Show me!')

get_average([2])
# # the output will be 2.0
# # because the function returns the average value
# # but the print statement after the return statement will not be executed
# # because the return statement exits the function


def is_first_last_equal(number_list):
  if len(number_list) == 0:
    return
  if number_list[0] == number_list[-1]:
    return True
  else:
    return False
print(is_first_last_equal([1, 2, 3, 1]))  # the output will be True
print(is_first_last_equal([1, 2, 3, 4]))  # the output will be False
print(is_first_last_equal([]))  # the output will be None
# # the function returns None when the list is empty
# # because there is no first and last element to compare