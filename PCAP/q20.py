# What is the expected behavior of the following snippet?
def gen():
    lst = range(5)
    for i in lst:
        yield i*i
for i in gen():
    print(i, end="")

# Step-by-Step Execution:
# Line 1-4: Generator Function Definition (gen())

# gen() is a generator function (because it contains yield).

# lst = range(5) creates an iterable [0, 1, 2, 3, 4] (in Python 3, range(5) is a sequence, not a list).

# The for loop iterates over lst, and for each i, it yields i * i (the square of i).

# Line 5-6: Using the Generator

# for i in gen(): starts iterating over the generator.

# Each time the generator is iterated, it yields the next value (0, 1, 4, 9, 16).

# print(i, end="") prints each value without spaces or newlines (end="" suppresses the default newline).

# Expected Output:
# 014916