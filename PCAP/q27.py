# What is the expected output of the following code?
class A:
    def __init__(self, name):
        self.name = name

a = A('class')
print(a)


# Explanation
# Class Definition: We define class A with an __init__ method that sets an instance variable name.

# Object Creation: We create an instance a of class A with 'class' as the name parameter.

# Printing the Object: When we print a, Python uses the default __str__ method which returns a string containing:

# The class name (A)

# The memory address of the object (hexadecimal value like 0x000001E3F7D1AFA0)

# Visualization

# [ Class Definition ]
# +-------------------+
# |      class A      |
# |-------------------|
# | __init__(self,name)|
# |   self.name = name |
# +-------------------+

# [ Object Creation ]
# a = A('class')
# +-------------------+
# |   Object a        |
# |-------------------|
# | name: 'class'     |
# +-------------------+

# [ Printing ]
# print(a) → No custom __str__ → Default output:
# <__main__.A object at 0x...>

# # The output will look something like:
# <__main__.A object at 0x7f9e8c4d1a90>