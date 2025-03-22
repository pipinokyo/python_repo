import sys

user_name = input('What is your name? ')
if user_name == '':
    # If the user does not enter a name, exit the program
    print('Empty name? I cannot work with that. I am clossing the program.')
    sys.exit()
print('Hello', user_name, '!')
print('Let us get started...')

# The following code is an example of how to handle exceptions in Python.
#  if I put empty input, the program will exit with an error message

# keyboard interrupt
while True:
    print('hi')
# this will run forever until you press Ctrl+C to stop it
# # # this will raise a KeyboardInterrupt exception
# # # and the program will exit with an error message


# index error
my_list = [1, 2, 3]
print(my_list[3])
# this will raise an IndexError exception
# because the index 3 is out of range for the list


# key error
my_dict = {'a': 1, 'b': 2}
print(my_dict['c'])
# this will raise a KeyError exception
# # # because the key 'c' does not exist in the dictionary


# type error
print('hello' + 5)
# this will raise a TypeError exception
# because you cannot concatenate a string and an integer
# # # you can only concatenate strings with strings


# value error
int('hello')
# this will raise a ValueError exception
# because you cannot convert a string that does not represent a number to an integer


# zero division error
print(5 / 0)
# this will raise a ZeroDivisionError exception
# because you cannot divide a number by zero