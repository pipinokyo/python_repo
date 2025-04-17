# What is the expected output of the following code?

def func(num):
    res = '*'
    for _ in range(num):
        res += res
    return res

for x in func(2):
    print(x, end='')