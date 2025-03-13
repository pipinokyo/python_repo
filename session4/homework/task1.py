# Task 1: Reverse a List
# Write a program that reverses a list using a for loop.
# Example:
# # Input:
# Enter numbers separated by space: 1 2 3 4 5
# # Output:
# Reversed List: [5, 4, 3, 2, 1]

# using for loop
list = input('Enter numbers separated by space: ').split() # .split() splits the input into as list based on spaces
print("list before reverse : ", list)
reversed_list = [] # empty list to store the reversed version of the original list
for i in list: ## iterates over each element (i) in the original list (list)
    reversed_list = [i] + reversed_list # if we do not put [] around i it will give us error because we cannot concatenate a string (i) with a list
print('list after reverse: ', reversed_list)


# using reverse() method
list = input('Enter numbers separated by space: ').split()
print("list before reverse : ", list)
list.reverse()
print('list after reverse: ', list)


# Using slicing
list = input('Enter numbers separated by space: ').split()
print("list before reverse : ", list)
print('list after reverse: ', list[::-1])