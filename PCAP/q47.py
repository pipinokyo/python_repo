# What is the expected output of the following code?

class A:
    def __init__(self):
        self.i = 0
        self.calc(10)
        print('i from A is', self.i)

    def calc(self, i):
        self.i = 2 * i

class B(A):
    def __init__(self):
        super().__init__()

    def calc(self, i):
        self.i = 3 * i

b = B()


# Explanation with Visualization
# This code demonstrates Python class inheritance and method overriding. Here's what happens when b = B() is executed:

# Initialization Flow:

# B() → B.__init__() → A.__init__() → B.calc()
# Step-by-Step Execution:

# We create an instance of class B: b = B()

# B's __init__ calls super().__init__(), which invokes A's __init__

# Inside A's __init__:

# self.i is set to 0

# self.calc(10) is called - but crucially, self is an instance of B

# Because of method overriding, B's calc() is called (not A's)

# B's calc() sets self.i = 3 * 10 = 30

# The print statement in A's __init__ shows "i from A is 30"

# Visualization:

# +----------------+       +----------------+
# |      Class A   |       |      Class B   |
# |----------------|       |----------------|
# | __init__(self) |       | __init__(self) |
# |   self.i = 0   |       |   super().__   |
# |   self.calc(10)|       |   init__()     |
# |   print(i)     |       |                |
# |                |       | calc(self, i)  |
# | calc(self, i)  |<------|   self.i=3*i   |
# |   self.i=2*i   |       |                |
# +--------^-------+       +----------------+
#          |
# Inheritance
# Output:
# The program will output: i from A is 30