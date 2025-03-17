# Loops are used to repeat an instruction or many instructions more than once.

# while condition: 
#     do_something()
# This syntax means so long as the condition is met, invoke the do something function repeatedly.

# counter = 1
# while counter < 11:
#     print(counter)
#     counter += 1
# print('Finished')

# the output
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# Finished

secret_number = 7
user_input = int(input('Try to guess the secret number from 0 to 10:'))
while user_input != secret_number:
  print('Wrong')
  user_input = int(input('Try to guess the secret number from 0 to 10:'))
print('correct')

# Try to guess the secret number from 0 to 10:5
# Wrong
# Try to guess the secret number from 0 to 10:4
# Wrong
# Try to guess the secret number from 0 to 10:7
# correct