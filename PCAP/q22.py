# What is the expected output of the following code?
x = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]

def func(data):
    res = data[0][0]
    for da in data:
        for d in da:
            if res < d:
                res = d
    return res

print(func(x[0]))