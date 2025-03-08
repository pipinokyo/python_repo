# Task 1: Number Comparison
# Write a program that takes two integer inputs and prints:
# "Both numbers are equal" if they are the same.
# "The first number is greater" if the first number is larger.
# "The second number is greater" if the second number is larger.


# 1. I need to set 2 variables
# 2. compare them if they equal or which on id greater

num1 = int(input("provide the first number please: "))
num2 = int(input("provide the second number please: "))

if num1 == num2:
    print("Both numbers are equal")
elif num1 > num2:
    print("The first number is greater")
else:
    print("The second number is greater")