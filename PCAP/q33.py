# What is the expected output of the following code?

class Test:
    def __init__(self, id):
        self.id = id
        id = 100

x = Test(23)
print(x.id)


# Explanation with Visualization
# 1. Class Definition
# class Test:
#     def __init__(self, id):
#         self.id = id  # Assigns the parameter id to the instance variable
#         id = 100     # Changes the local variable id, but doesn't affect instance
# 2. Object Creation and Output
# x = Test(23)  # Creates an instance of Test with id=23
# print(x.id)   # Prints the instance variable id
# Visualization
# Before __init__ is called:

# x (uninitialized object)
# During __init__(self, id) call (id=23):

# Local namespace:
# self → points to x object
# id → 23
# After self.id = id:
# x object:
#   id: 23

# Local namespace:
#   id: 23 (about to be changed)
# After id = 100:
# x object:
#   id: 23 (unchanged)

# Local namespace:
#   id: 100 (but this is local and discarded when __init__ ends)
# Final state:
# x object:
#   id: 23

# Output
# The script will output: 23