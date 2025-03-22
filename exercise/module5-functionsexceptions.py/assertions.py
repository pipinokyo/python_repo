# what if we want to raise exceptions by ourselves?
# Take a look at the following program.

def calculate_inverse(number):
    assert (number !=0), 'Got 0 as number!'
    return 1/number

# This simple function uses a new keyword assert.
# After this keyword, we put one or more conditions inside reference brackets.
# These are conditions that we assume should always be true.
# This specific function to work correctly if the condition or conditions are true.
# Python simply moves on to the next line.
# But if the condition is not true, then Python shows an error with the error message that we specify after a comma
# Let's see how that program works in practice.


def calculate_inverse(number):
    assert (number !=0), 'Got 0 as number!'
    return 1/number

calculate_inverse(5)
#  the output will be 0.2 --everything is fine 

# And now with zero.

def calculate_inverse(number):
    assert (number !=0), 'Got 0 as number!'
    return 1/number

calculate_inverse(0)
# And a new kind of exception appeared.
# AssertionError : Got 0 as number!



# Assertions are a simple concept, but it's important to understand when we should and should not use them
# In general, assertions are used for debugging and testing of code.
# Assertions are also sometimes used to document your code.
# This way you can communicate to other developers what you expect in your functions.
# On the other hand, you should not use assertions for validating user input.
# That's because it's impossible to turn off assertions when you publish a program to your users.
# Turning off assertions in this case would mean that you lose all the code that validates user input.
# Apart from that, assertions are not an error handling tool.
# The purpose is to notify you about bugs during development so you can catch and fix bugs quickly.