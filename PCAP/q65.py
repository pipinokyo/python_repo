# What is the expected output of the following code?

class A:
    def __init__(self, x=0):
        self.x = x
    
    def func(self):
        self.x += 1

class B(A):
    def __init__(self, y=0):
        A.__init__(self, 3)
        self.y = y

    def func(self):
        self.y += 1

b = B()
b.func()
print(b.x, b.y)


# Class Definitions:
# Class A:

# __init__: Initializes an instance with x set to 0 by default (or a provided value).

# func: Increments self.x by 1.

# Class B (inherits from A):

# __init__: Calls A.__init__ with x=3, then initializes y to 0 by default (or a provided value).

# func: Overrides A.func and increments self.y by 1 instead of self.x.

# Execution Flow:
# b = B():

# B.__init__ is called.

# Inside B.__init__, A.__init__(self, 3) sets b.x = 3.

# Then, self.y = 0 sets b.y = 0.

# State: b.x = 3, b.y = 0.

# b.func():

# This calls B.func (not A.func because it's overridden).

# self.y += 1 increments b.y from 0 to 1.

# b.x remains unchanged (3).

# State: b.x = 3, b.y = 1.

# print(b.x, b.y):

# Outputs 3 1.

# Visualization:
# Step	    Action	          b.x	        b.y
# 1	        b = B()	           3	         0
# 2	        b.func()	       3             1
# 3	        print(b.x, b.y)	 Output: 3 1