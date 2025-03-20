numbers = [1,2,3,4]

# Let's say we want to have a list with numbers from 1 to 100.
# you could think of using a loop the following way.

numbers = []
for i in range(1,101):
    numbers.append(i)
print(numbers)

# First we create an empty list, then inside a for loop, we append numbers to it.
# That certainly does the job, but it takes a lot of space.

# Python has a unique feature designed to speed up this process of creating a list.
# The feature is called List comprehension.

numbers = [i for i in range(1,101)]
print(numbers)
# This code also creates a list for us, but it just takes one line to do so.
# Note that we had to add the control variable name in front of the loop.
# Remember about this because otherwise you'll see the following error invalid syntax.

# we now want to generate numbers from 1 to 100 again, but we want to skip numbers that are divisible by three.
numbers = [i for i in range(1,101) if i % 3 != 0]
print(numbers)