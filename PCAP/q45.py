# What is the expected output of the following code?

data = [261, 321]
try:
    print(data[-3])
except Exception as exception:
    print(exception.args)
else:
    print("('success',)")