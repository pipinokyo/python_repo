# Task 2: Number Swapper
# Write a Python program that takes two numbers as input from the user and swaps their values.

# take the input from the user
num1 = input("first number: ")
num2 = input("second number: ")
# display the original values
print("before swapping: \nnumber1 is:", num1,"\nnumber2 is:", num2)
# swap the values
num1, num2 = num2, num1
# display the swap values
print("after swapping: \nnumber1 is:", num1,"\nnumber2 is:", num2)