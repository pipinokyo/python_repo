# What is the expected behavior of the following snippet?

class Team:
    def show_ID(self):
        print(self.get_ID())

    def get_ID(self):
        return "anonymous"
    
class A(Team):
    def get_ID(self):
        return "Alpha"
    

a = A()
a.show_ID()


# Class Definitions:

# First, we define a base class Team with two methods:
# show_ID(self): Prints the result of self.get_ID()
# get_ID(self): Returns the string "anonymous"
# Then we define a subclass A that inherits from Team and overrides get_ID() to return "Alpha" instead.

# Object Creation:
# a = A() creates an instance of class A.

# Method Call:
# When we call a.show_ID(), here's what happens:
# Python first looks for show_ID in class A - not found
# Then looks in parent class Team - found
# Executes Team.show_ID(a) (passing our instance as self)
# Inside show_ID, it calls self.get_ID()
# Even though we're in Team's method, self is still our A instance
# So Python looks for get_ID starting from A's class
# Finds A.get_ID() which returns "Alpha"
# This result is then printed

# Output:
# The code will print: Alpha