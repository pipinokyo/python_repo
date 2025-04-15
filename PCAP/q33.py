# What is the expected output of the following code?

class Test:
    def __init__(self, id):
        self.id = id
        id = 100

x = Test(23)
print(x.id)