# Consider the following file module.py.

module.py:
print(__name__)

# What will be the output, if you run it?

# Understanding __name__ in Python
# In Python, __name__ is a special built-in variable that holds the name of the current module. Its value depends on how the module is being used:

# When a module is run directly (like python module.py):

# __name__ is set to "__main__".

# When a module is imported (like import module in another script):

# __name__ is set to the name of the module (in this case, "module").

# Step-by-Step Execution
# Since you're running module.py directly (not importing it), here's what happens:

# Python starts executing module.py.

# It encounters the line print(__name__).

# Because the script is being run directly, __name__ is "__main__".

# Thus, print(__name__) prints "__main__".

# Output
# The output will be:

# __main__