# It's extremely difficult to write computer programs that never fail and contain no errors.
# One of the most popular errors, which I'm sure you've seen already, is the syntax error.
# for example, when you forget to indent code in your if statement, take a look.
if True:
print('Hello') 
# # this will raise a syntax error because the print statement is not indented

# A ready made Python program should not contain any syntax errors at all.
# However, sometimes there are errors generated through no fault of your own.
# For instance, you may ask a user to provide a number and they provide something else instead.
# In such situations, you will see a different kind of error.
# Let's see that in practice.

value = int(input('Please enter a number: '))
print('the inverse of', value, 'is', 1 / value)
# # if the user enters a number, the program will run fine
# # but if the user enters a string, the program will raise a ValueError
# # because the int() function cannot convert a string to an integer

# You may think of exceptions as just any kind of errors that Python generates,
# but a more formal definition is as follows.
# An exception is an event which occurs during the execution of a program that disrupts the normal flow of the program's instructions.
 
# There are many situations where you can somehow handle the exception and react to it so that the program execution continues normally.
# To handle exceptions, we need to use a new special kind of structure.
# Try except take a look at the program.

try:
    # this is the code that may raise an exception
    value = int(input('Please enter a number: '))
    print('the inverse of', value, 'is', 1 / value)
except:
    # this is the code that will run if an exception occurs
    print('Please enter a valid number.')
# # if the user enters a number, the program will run fine
# # but if the user enters a string, the program will print 'Please enter a valid number.'
# # and the program will continue to run without crashing
# # this is because the except block catches the exception and handles it

# # you can also specify the type of exception you want to catch
try:
    # this is the code that may raise an exception
    value = int(input('Please enter a number: '))
    print('the inverse of', value, 'is', 1 / value)
except ValueError:
    # this is the code that will run if a ValueError occurs
    print('Please enter a valid number.')
# # if the user enters a number, the program will run fine
# # but if the user enters a string, the program will print 'Please enter a valid number.
# and the program will continue to run without crashing
#  if the user enters 0, the program will raise a ZeroDivisionError
# # because we cannot divide by zero
# # we can handle this exception as well
try:
    # this is the code that may raise an exception
    value = int(input('Please enter a number: '))
    print('the inverse of', value, 'is', 1 / value)
except ZeroDivisionError:
    # this is the code that will run if a ZeroDivisionError occurs
    print('You cannot divide by zero.')