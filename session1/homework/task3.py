# Task 3: Simple Calculator
# Create a calculator that takes two numbers and an operator (+, -, *, /, //, %, **) as input and performs the appropriate calculation.

# first we need to take input from the user
# we need to convert the data to int or float to be able to do calculations

num1 = float(input("first number: "))
operator = input("Enter the operator (+ - * / // % **): ")
num2 = float(input("second number: "))

# we need to check the value of the operator variable and decide which
#arithmetic operation to perform based on user's input
if operator == "+":
    result = num1 + num2
    print(num1, "+", num2, "=", result)
elif operator == "-":
    result = num1 - num2
    print(num1, "-", num2, "=", result)
elif operator == "*":
    result = num1 * num2
    print(num1, "*", num2, "=", result)
elif operator == "/":
    result = num1 / num2
    print(num1, "/", num2, "=", result)
elif operator == "//":
    result = num1 // num2
    print(num1, "//", num2, "=", result)
elif operator == "%":
    result = num1 % num2
    print(num1, "%", num2, "=", result)
elif operator == "**":
    result = num1 ** num2
    print(num1, "**", num2, "=", result)
# the else ensures that if the users enters an invalid operator
else:
    print (operator, "is not a valid operator")