# What is the expected output of the following code?

class Test:
    def __init__(self, s='Welcome'):
        self.s = s
        
    def print(self):
        print(self.s)

x = Test()
x.print()

# Explanation:
# Class Definition:
# class Test: - Defines a new class named "Test"

# def __init__(self, s='Welcome'): - Constructor method that initializes new objects

# Takes a parameter s with default value 'Welcome'

# self.s = s assigns the parameter to an instance variable

# Methods:
# def print(self): - Defines a method named "print"

# print(self.s) - Prints the value of the instance variable s

# Object Creation and Method Call:
# x = Test() - Creates an instance of the Test class using default parameter

# x.print() - Calls the print method on the x object

# Visualization:
# +---------------------+
# |       Class Test    |
# +---------------------+
# | __init__(s='Welcome')|
# | print()             |
# +---------------------+
#          ^
#          |
#          |
# +---------------------+
# |      Object x       |
# +---------------------+
# | s = 'Welcome'       |
# +---------------------+
# Expected Output:
# When you run this code, it will output:  Welcome