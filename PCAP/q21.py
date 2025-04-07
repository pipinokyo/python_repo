# What is the expected output of the following code?
x = 0
try:
    print(x)
    print(1 / x)
except ZeroDivisionError:
    print("ERROR MESSAGE")
finally:
    print(x + 1)
print(x + 2)


# Initialization:
# x = 0
# x is assigned the value 0.

# Try Block:
# try:
#     print(x)
#     print(1 / x)
# print(x) executes first, printing 0.

# Then print(1 / x) attempts to compute 1 / 0, which raises a ZeroDivisionError.

# Except Block:
# except ZeroDivisionError:
#     print("ERROR MESSAGE")
# The ZeroDivisionError is caught, and "ERROR MESSAGE" is printed.

# Finally Block:
# finally:
#     print(x + 1)
# The finally block always executes, regardless of whether an exception occurred.

# x + 1 is 0 + 1, so 1 is printed.

# After the Try-Except-Finally:
# print(x + 2)
# This is outside the exception handling, so it executes normally.

# x + 2 is 0 + 2, so 2 is printed.

# Final Output:
# 0
# ERROR MESSAGE
# 1
# 2