# you must take an integer input, if user gives any other data type output the following
# output: invalid input! Pleae enter an integer

inp = input("Enter an integer: ")
try:
    inp = int(inp)
    print(f"You entered the integer: {inp}")
except ValueError:
    print("Invalid input! Please enter an integer.")