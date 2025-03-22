# Recursion takes place when a function calls itself.
# This idea may seem very simple in theory, but is a bit more difficult to understand in practice.

# We have the following problem.
# We want to write a function to provide the factorial for a given number.

# factorial = 3!# factorial = 3 * 2 * 1
# factorial = 3 * 2 * 1 = 6
# factorial = 4!# factorial = 4 * 3 * 2 * 1
# factorial = 4 * 3 * 2 * 1 = 24
# factorial = 5!# factorial = 5 * 4 * 3 * 2 * 1
# factorial = 5 * 4 * 3 * 2 * 1 = 120

# let's write a function that calculates the factorial for a given number.
# We'll write two versions of this function. One without recursion and one with recursion.

# We'll start with the version that doesn't involve recursion.
def get_factorial(number):
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    return factorial
# let's test the function
print('The factorial of 3 is:', get_factorial(3))  # the output will be 6
print('The factorial of 4 is:', get_factorial(4))  # the output will be 24

# with recursion.
def get_factorial_recursive(number):
    if number == 0 or number == 1:  # base case
        return 1
    else:
        return number * get_factorial_recursive(number - 1)  # recursive case
# let's test the function
print('The factorial of 3 is:', get_factorial_recursive(3))  # the output will be 6
print('The factorial of 4 is:', get_factorial_recursive(4))  # the output will be 24
print('The factorial of 5 is:', get_factorial_recursive(5))  # the output will be 120

# To understand how that works, let's try to behave like Python's interpreter and break it down step by step.
# When we call get_factorial_recursive(5), it checks if 5 is 0 or 1.
# Since it's not, it goes to the else statement and returns 5 * get_factorial_recursive(4).
# Now, it needs to calculate get_factorial_recursive(4).
# It checks if 4 is 0 or 1. Since it's not, it goes to the else statement and returns 4 * get_factorial_recursive(3).
# Now, it needs to calculate get_factorial_recursive(3).
# It checks if 3 is 0 or 1. Since it's not, it goes to the else statement and returns 3 * get_factorial_recursive(2).
# Now, it needs to calculate get_factorial_recursive(2).
# It checks if 2 is 0 or 1. Since it's not, it goes to the else statement and returns 2 * get_factorial_recursive(1).
# Now, it needs to calculate get_factorial_recursive(1).
# It checks if 1 is 0 or 1. Since it is, it returns 1.
